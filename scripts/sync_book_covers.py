#!/usr/bin/env python3
"""Cache actual published book cover images under assets/covers and update README.

Only downloads third-party book-cover artwork; it never generates replacements.
Existing images are retained if no trustworthy source can be fetched.
"""
import concurrent.futures
import io
import json
import re
from pathlib import Path
from urllib.parse import urlparse, quote

import requests
from PIL import Image, ImageOps, ImageChops, UnidentifiedImageError

BOOKS = json.loads(r'''[["2026","01","失去的胜利",["https://www.books.com.tw/img/001/090/04/0010900449.jpg"]],["2026","02","我甚至相信你拥有整个宇宙",["https://www.books.com.tw/img/CN1/796/15/CN17961544.jpg"]],["2026","03","道德情操论",["https://www.books.com.tw/img/CN1/011/37/CN10113715.jpg"]],["2026","04","人妻约会指南",["https://www.bktai.com/upload/202511/25110310393777.webp","https://pica.zhimg.com/80/v2-6f8174feeb1e9a8fee1716ebf6233dd2_720w.webp"]],["2026","05","被讨厌的勇气",["https://www.books.com.tw/img/001/065/31/0010653153.jpg","https://img.alicdn.com/bao/uploaded/i1/2208191633869/O1CN01j5XiC11eS3AV1LplE_%21%210-item_pic.jpg"]],["2026","06","猎豹",["https://pic2.zhimg.com/v2-b97fa8dba7c777f58f5dce9cb6abc155_1440w.jpg","https://s.eslite.com/upload/product/o/2680791222003/ec705125.jpg"]],["2026","07","铁血残明",["https://bookcover.yuewen.com/qdbimg/349573/1024424884/600"]],["2026","08","经济学的思维方式",["https://motatabooks.com/cdn/shop/files/a7146c15-d2a8-40aa-ae30-54606b49534d.png?v=1762395352"]],["2025","01","玻璃之锤",["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJGr7pXvqynMKJjPko8C7mje5DDuy37ogErQ&s","https://www.chinesebookonline.com/file/2158059/354401-800x800-bo-li-zhi-chui-jpg.jpg"]],["2025","02","雅思词汇真经",["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgiwFTwT15ihQ2sI9pHspZb8Lcbr7G3swF6Q&s"]],["2025","03","如首无作祟之物",["https://www.books.com.tw/img/001/092/78/0010927819.jpg","https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1676715664i/65141795.jpg"]],["2025","04","浪潮之巅",["https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1345477434i/12673959.jpg"]],["2025","05","福尔摩斯探案集",["https://www.books.com.tw/img/001/052/73/0010527328.jpg"]],["2025","06","100个Go语言典型错误",["https://www.manongbook.com/d/file/other/b842ee0ffcff5399d8fd2c5f03d9746d0.jpg","https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1639543467i/58571862.jpg"]],["2025","07","软件设计的哲学",["https://img2024.cnblogs.com/blog/121186/202502/121186-20250207104655030-663263026.jpg","https://media.s-bol.com/qW7oYWWyOrw0/XDnZwkV/972x1200.jpg"]],["2025","08","双月城的惨剧",["https://www.books.com.tw/img/CN1/191/01/CN11910193.jpg"]],["2025","09","情书",["https://www.books.com.tw/img/001/054/64/0010546476.jpg"]],["2025","10","Go专家编程",["https://cf-assets2.tenlong.com.tw/products/images/000/150/499/original/9787121365577.jpg"]],["2025","11","Dubliners",["https://www.aliceandbooks.com/covers/Dubliners-James_Joyce-md.png"]],["2025","12","JavaScript高级程序设计（第4版）",["https://file.ituring.com.cn/LargeCover/20080d81a4fb8a268c40"]],["2025","13","了凡四训",["https://cdn.kobo.com/book-images/e5f37091-2524-444e-8bd1-5d3a3c8058df/353/569/90/False/hiDeSoxTXj-i8Vdetou-2Q.jpg"]],["2025","14","万历十五年",["https://chinabook.co.kr/data/goods/1/2017/10/7866_tmp_db7ca48e05dc4cb3021a371128cadf557988view.jpg"]],["2025","15","理解人性",["https://img3.od-cdn.com/ImageType-100/8143-1/%7B2222346E-B4CE-45B1-A80A-C7826685859A%7DIMG100.JPG"]],["2025","16","雪人",["https://img.alicdn.com/imgextra/i2/3310271582/O1CN015xpLpv1NYbc2Zb0pF_!!4611686018427386974-2-item_pic.png"]],["2025","17","以日为鉴",["https://www.kaimingpress.com/backadmin/bookcover/1760921954814.png","https://gw.alicdn.com/imgextra/i2/725677994/O1CN01huZqS728vJEhaPE6k_!!4611686018427385770-2-item_pic.png_.webp"]],["2025","18","失去的三十年：平成日本经济史",["https://www.books.com.tw/img/CN1/784/17/CN17841751.jpg"]]]''')
README = Path("README.md")
COVER_ROOT = Path("assets/covers")
UA = "Mozilla/5.0 (compatible; ReaderInAllTimeCoverCache/1.0; +https://github.com/LiRongji1995/ReaderInAllTime)"

def download_one(entry):
    year, idx, title, urls = entry
    path = COVER_ROOT / year / (idx + ".jpg")
    if path.is_file() and path.stat().st_size > 1500:
        return (year, idx, title, str(path), "already present", None)
    errors = []
    extended_urls = []
    for candidate in urls:
        extended_urls.append(candidate)
        if candidate.startswith("https://www.books.com.tw/img/"):
            extended_urls.append("https://im1.book.com.tw/image/getImage?h=720&i=" + quote(candidate, safe="") + "&w=620")
    for url in extended_urls:
        try:
            host = urlparse(url).netloc
            headers = {"User-Agent": UA, "Accept": "image/avif,image/webp,image/png,image/jpeg,image/*;q=0.8,*/*;q=0.1"}
            if host.endswith("books.com.tw"): headers["Referer"] = "https://www.books.com.tw/"
            if "zhimg.com" in host: headers["Referer"] = "https://www.zhihu.com/"
            r = requests.get(url, headers=headers, timeout=(10, 22), allow_redirects=True)
            r.raise_for_status()
            if len(r.content) < 700 or len(r.content) > 15_000_000:
                raise ValueError(f"unexpected size {len(r.content)}")
            im = Image.open(io.BytesIO(r.content))
            im.load()
            im = ImageOps.exif_transpose(im)
            if min(im.size) < 65 or max(im.size) < 110:
                raise ValueError(f"image too small: {im.size}")
            if im.mode != "RGB":
                background = Image.new("RGB", im.size, "white")
                if im.mode in ("RGBA", "LA"):
                    background.paste(im.convert("RGBA"), mask=im.convert("RGBA").getchannel("A"))
                else:
                    background.paste(im.convert("RGB"))
                im = background
            im.thumbnail((650, 950), Image.Resampling.LANCZOS)
            path.parent.mkdir(parents=True, exist_ok=True)
            im.save(path, "JPEG", quality=87, optimize=True, progressive=True)
            return (year, idx, title, str(path), url, None)
        except (OSError, ValueError, requests.exceptions.RequestException, UnidentifiedImageError) as ex:
            errors.append(f"{host}: {str(ex)[:85]}")
    return (year, idx, title, None, None, " | ".join(errors))


def tidy_covers():
    # These retailer thumbnails have substantial artificial white padding.
    # Crop only the background margins, preserving the real printed cover.
    crop_targets = {("2026", "03"), ("2026", "08"), ("2025", "05"), ("2025", "09"), ("2025", "17")}
    for year, idx in crop_targets:
        path = COVER_ROOT / year / (idx + ".jpg")
        if not path.is_file(): continue
        with Image.open(path) as source:
            image = source.convert("RGB")
        w, h = image.size
        diff = ImageChops.difference(image, Image.new("RGB", (w,h), "white"))
        bbox = ImageOps.grayscale(diff).point(lambda v: 255 if v >= 36 else 0).getbbox()
        if not bbox: continue
        left, top, right, bottom = bbox
        if (right-left)/w > 0.91 and (bottom-top)/h > 0.91: continue
        if right-left < 90 or bottom-top < 120: continue
        pad = max(4, int(min(right-left,bottom-top)*0.018))
        left,top,right,bottom=max(0,left-pad),max(0,top-pad),min(w,right+pad),min(h,bottom+pad)
        cropped = image.crop((left,top,right,bottom))
        if cropped.size != image.size:
            cropped.save(path, "JPEG", quality=88, optimize=True, progressive=True)
            print(f"CROPPED {year}/{idx}: {(w,h)} -> {cropped.size}", flush=True)

def existing_sources():
    source_path = COVER_ROOT / "SOURCES.md"
    if not source_path.is_file(): return {}
    entries = {}
    for line in source_path.read_text(encoding="utf-8").splitlines():
        m = re.search(r'^- \\*\\*(\\d{4}) (\\d{2}) · ([^*]+)\\*\\*: .* · source: (https?://\\S+)', line)
        if m: entries[(m.group(1),m.group(2))] = m.group(4)
    return entries

def main():
    assert len(BOOKS) == 26
    readme = README.read_text(encoding="utf-8")
    known_sources = existing_sources()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = sorted(pool.map(download_one, BOOKS), key=lambda x: (x[0],x[1]), reverse=True)
    good = 0
    bad = []
    report = ["# Original book-cover sources", "", "All images are real publisher-edition or author-released cover artwork, not AI-generated artwork or illustrative placeholders. Cover rights remain with their respective rights holders.", "Displayed editions can differ from editions personally read where the edition was not specified.", ""]
    for year, idx, title, filename, source, error in results:
        pattern = r'(<img src=")([^"]+)(" height="\d+" alt="《' + re.escape(title) + r'》\s*封面")'
        if not re.search(pattern, readme):
            raise RuntimeError(f"Missing cover image for {title}")
        if filename:
            if source == "already present": source = known_sources.get((year, idx), "source unknown")
            readme, n = re.subn(pattern, lambda m: m.group(1) + "./" + filename + m.group(3), readme, count=1)
            if n != 1: raise RuntimeError(f"Failed replacement for {title}")
            good += 1
            report.append(f"- **{year} {idx} · {title}**: [image](../../{filename}) · source: {source}")
            print(f"OK   {year}/{idx} {title}: {source}", flush=True)
        else:
            bad.append(f"{year}/{idx} {title}: {error}")
            report.append(f"- **{year} {idx} · {title}**: not cached; original cover unavailable at download time")
            print(f"FAIL {year}/{idx} {title}: {error}", flush=True)
    README.write_text(readme, encoding="utf-8")
    tidy_covers()
    if good == len(BOOKS):
        for obsolete in COVER_ROOT.glob("cover-*.svg"):
            obsolete.unlink()
            print(f"REMOVED placeholder: {obsolete}", flush=True)
    (COVER_ROOT / "SOURCES.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"RESULT cached={good}/{len(BOOKS)} missing={len(bad)}", flush=True)
    if bad:
        print("UNRESOLVED:", *bad, sep="\n", flush=True)

if __name__ == "__main__":
    main()
