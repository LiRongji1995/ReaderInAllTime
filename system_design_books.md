<div align="center">

# 🧭 System Design Reading Guide

**From interview frameworks to production-ready systems.**

从“会画架构图”，到真正理解系统为什么这样设计。

<br>

![Updated](https://img.shields.io/badge/Updated-2026-6F4E37?style=flat-square)
![Books](https://img.shields.io/badge/Core_Books-14-8B6F47?style=flat-square)
![Topics](https://img.shields.io/badge/Topics-Architecture_%C2%B7_Distributed_Systems_%C2%B7_SRE-A68A64?style=flat-square)

</div>

---

## About

系统设计不是背诵组件名称，也不是把缓存、消息队列和微服务全部画进一张图。

真正重要的是：

- 从业务需求中提炼系统目标；
- 在性能、成本、复杂度与可靠性之间做取舍；
- 解释一个设计为什么适合当前场景；
- 预判系统在流量增长、依赖故障和数据膨胀之后会发生什么。

这份书单按学习目标与难度整理，既适合准备系统设计面试，也适合希望提升架构能力、分布式系统基础和生产工程经验的开发者。

<div align="center">

[快速选择](#快速选择) ·
[完整书单](#完整书单) ·
[12 周学习路径](#12-周学习路径) ·
[系统设计检查清单](#系统设计检查清单)

</div>

---

## 快速选择

不必一次读完所有书。先根据目标选择一条路线。

| 你的目标 | 推荐路线 |
|---|---|
| **短期准备系统设计面试** | Alex Xu Vol. 1 → Vol. 2 → 每周完成 2 个 Mock Design |
| **建立系统设计基础** | *Fundamentals of Software Architecture* → *Designing Data-Intensive Applications* |
| **深入分布式系统与数据层** | *Designing Data-Intensive Applications* → *Designing Distributed Systems* → *Database Internals* |
| **学习微服务与架构演进** | *Building Microservices* → *Monolith to Microservices* → *Software Architecture: The Hard Parts* |
| **提升生产可靠性能力** | *Release It!* → *Site Reliability Engineering* → *The Site Reliability Workbook* |
| **兼顾安全与可靠性** | *Building Secure & Reliable Systems* |

> **最小核心路线：**  
> Alex Xu Vol. 1 → DDIA → Fundamentals of Software Architecture → Release It! → Google SRE

---

# 完整书单

## 01 · 面试框架与表达

这一部分帮助你建立答题结构、容量估算意识，以及常见互联网系统的分析方法。

### 1. [System Design Interview – An Insider's Guide, Volume 1](https://blog.bytebytego.com/p/system-design-interview-books-volume)

**作者：** Alex Xu  
**难度：** 入门  
**定位：** 系统设计面试框架与经典题型  
**优先级：** ⭐ 核心

你会接触到限流器、短链接、聊天系统、新闻流、文件存储等高频题目，并学习如何把一个模糊问题拆解为：

1. 功能与非功能需求；
2. 粗略容量估算；
3. API 与数据模型；
4. 高层架构；
5. 瓶颈、扩展与取舍。

**建议读法：** 不要只看答案。每章开始前先独立设计 30 分钟，再与书中的方案对照。

---

### 2. [System Design Interview – An Insider's Guide, Volume 2](https://blog.bytebytego.com/p/system-design-interview-books-volume)

**作者：** Alex Xu、Sahn Lam  
**难度：** 入门至中级  
**定位：** 更多复杂系统案例  
**优先级：** 推荐

第二卷与第一卷不是简单的上下册关系，而是覆盖另一组设计题。适合在掌握基本答题框架后继续扩展案例库。

**建议读法：** 重点关注不同系统之间重复出现的模式，例如：

- 异步处理；
- 分区与复制；
- 幂等性；
- 热点处理；
- 最终一致性；
- 限流与背压。

---

### 3. [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)

**类型：** 在线课程  
**难度：** 入门  
**定位：** 图文式、交互式面试学习  
**优先级：** 选读

它不是传统书籍，但适合希望以较轻量方式快速进入系统设计题型的人。若已经完整阅读 Alex Xu 两卷并持续练习，通常不必再把所有同类课程全部学一遍。

---

## 02 · 架构基础与权衡

这一部分关注架构师如何思考，而不只是某一种具体技术。

### 4. [Fundamentals of Software Architecture, 2nd Edition](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)

**作者：** Mark Richards、Neal Ford  
**难度：** 中级  
**定位：** 软件架构全景与架构思维  
**优先级：** ⭐ 核心

本书系统讨论：

- 架构特性与非功能需求；
- 模块化、耦合与内聚；
- 分层、事件驱动、微服务等架构风格；
- 架构决策记录；
- 风险分析；
- 架构图与沟通表达。

**适合谁：** 已经能够独立开发功能，但希望开始从系统整体、团队协作与长期演进角度思考的工程师。

**建议读法：** 结合自己做过的项目，为其补写一份架构特性清单和 Architecture Decision Record（ADR）。

---

### 5. [Software Architecture: The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)

**作者：** Neal Ford、Mark Richards、Pramod Sadalage、Zhamak Dehghani  
**难度：** 中高级  
**定位：** 分布式架构中的困难决策  
**优先级：** ⭐ 核心

它重点讨论那些不存在标准答案的问题：

- 服务应该拆多细；
- 数据所有权如何划分；
- 分布式事务如何处理；
- 编排与协同如何选择；
- 服务之间如何共享或隔离数据；
- 如何评估架构方案中的取舍。

**建议读法：** 在读完架构基础后再读。每个章节都尝试写下“在什么条件下，我会选择相反方案”。

---

### 6. [The Art of Scalability, 2nd Edition](https://www.oreilly.com/library/view/art-of-scalability/9780134031408/)

**作者：** Martin L. Abbott、Michael T. Fisher  
**难度：** 中高级  
**定位：** 可扩展性、组织与工程流程  
**优先级：** 选读

它的价值不只在于技术扩展，也在于把系统、团队和组织结构放在同一个尺度上讨论。书中部分技术案例较早，但关于扩展模型、组织职责和故障治理的思想仍然有参考价值。

---

## 03 · 数据密集型与分布式系统

这是系统设计最重要的理论主线之一。

### 7. [Designing Data-Intensive Applications, 2nd Edition](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)

**作者：** Martin Kleppmann、Chris Riccomini  
**难度：** 中高级  
**定位：** 数据系统与分布式系统核心原理  
**优先级：** ⭐ 必读

常见简称为 **DDIA**。第二版进一步纳入了现代数据系统与云环境中的新变化。

核心主题包括：

- 数据模型与查询语言；
- 存储引擎与索引；
- 编码与数据演进；
- 复制与分区；
- 事务与一致性；
- 分布式系统故障；
- 批处理与流处理；
- 数据架构中的长期取舍。

**建议读法：**

- 第一遍建立概念地图，不必强求记住所有细节；
- 第二遍围绕具体问题回读，例如“为什么需要共识”“何时使用异步复制”；
- 每章整理一张“方案—优势—代价—适用条件”表格。

---

### 8. [Designing Distributed Systems, 2nd Edition](https://www.oreilly.com/library/view/designing-distributed-systems/9781098156343/)

**作者：** Brendan Burns  
**难度：** 中级  
**定位：** 可复用的分布式系统设计模式  
**优先级：** 推荐

相比 DDIA 更偏向工程模式与组件组合，适合学习：

- Sidecar、Ambassador、Adapter 等单节点模式；
- 复制、分片与领导者选举；
- 工作队列；
- 批处理与事件驱动；
- 面向容器环境的分布式应用设计。

**适合谁：** 希望把分布式理论转化为可落地工程结构的人。

---

### 9. [Database Internals](https://www.oreilly.com/library/view/database-internals/9781492040330/)

**作者：** Alex Petrov  
**难度：** 高级  
**定位：** 数据库存储与分布式数据库内部机制  
**优先级：** 进阶选读

内容涵盖：

- B-Tree 与 LSM-Tree；
- 页、日志与恢复；
- 缓冲、索引和存储布局；
- 复制、故障检测与共识；
- 分布式事务。

**建议读法：** 先读 DDIA，再读本书。它更适合想理解数据库“内部为什么这样工作”的读者，而不是系统设计的第一本书。

---

## 04 · 微服务与架构演进

微服务不是默认答案。这部分重点是理解何时拆分、如何拆分，以及拆分之后新增的复杂性。

### 10. [Building Microservices, 2nd Edition](https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/)

**作者：** Sam Newman  
**难度：** 中级  
**定位：** 微服务设计、交付与治理  
**优先级：** ⭐ 核心

主要主题包括：

- 服务边界；
- 通信方式；
- 数据拆分；
- 部署与测试；
- 可观测性；
- 安全；
- 组织结构；
- 微服务带来的复杂性。

**建议读法：** 阅读时始终追问：“这个问题在模块化单体中是否已经能够解决？”不要把服务数量当作架构成熟度。

---

### 11. [Monolith to Microservices](https://www.oreilly.com/library/view/monolith-to-microservices/9781492047834/)

**作者：** Sam Newman  
**难度：** 中高级  
**定位：** 从单体系统渐进迁移到微服务  
**优先级：** 推荐

本书比“如何从零设计微服务”更贴近现实，因为多数系统都需要在不中断业务的情况下逐步演进。

重点关注：

- 渐进式迁移；
- Strangler Fig Pattern；
- 数据库拆分；
- 依赖解耦；
- 过渡架构；
- 迁移成本与收益判断。

---

## 05 · 生产可靠性与故障设计

一个系统能够在演示环境运行，不代表它能够长期稳定地运行在生产环境。

### 12. [Release It!, 2nd Edition](https://www.oreilly.com/library/view/release-it-2nd/9781680504552/)

**作者：** Michael T. Nygard  
**难度：** 中级  
**定位：** 生产系统稳定性与故障隔离  
**优先级：** ⭐ 必读

本书通过真实故障模式讨论：

- 级联故障；
- 超时与重试；
- 熔断；
- 舱壁隔离；
- 背压；
- 慢依赖；
- 无界资源；
- 优雅降级。

**建议读法：** 每读一个稳定性模式，就检查自己维护的系统是否存在对应的反模式。

---

### 13. [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)

**作者：** Google SRE 团队  
**难度：** 中高级  
**定位：** 大规模系统的可靠性工程  
**优先级：** ⭐ 核心  
**阅读方式：** 官方免费在线阅读

核心概念包括：

- SLI、SLO 与错误预算；
- 风险管理；
- 监控与告警；
- 自动化；
- 容量规划；
- 变更管理；
- 故障响应；
- 消除重复劳动（Toil）。

**建议读法：** 不必从头顺序读完。可先读 SLO、监控、自动化、容量规划和事故响应相关章节。

---

### 14. [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/)

**作者：** Google SRE 团队及行业实践者  
**难度：** 中高级  
**定位：** SRE 方法的落地实践  
**优先级：** 推荐  
**阅读方式：** 官方免费在线阅读

它是 SRE 理论书的实践伴侣，提供更多具体案例，适合在理解 SLO、告警和事故管理之后阅读。

---

### 15. [Building Secure & Reliable Systems](https://google.github.io/building-secure-and-reliable-systems/raw/toc.html)

**作者：** Heather Adkins、Betsy Beyer 等  
**难度：** 中高级  
**定位：** 安全性与可靠性的统一设计  
**优先级：** 推荐  
**阅读方式：** 官方免费在线阅读

重点讨论：

- 最小权限；
- 可理解性；
- 韧性与恢复；
- 故障域与爆炸半径；
- 安全发布；
- 调查与审计；
- 安全事件响应。

这本书尤其适合负责身份认证、基础设施、安全平台或高可靠服务的工程师。

---

## 12 周学习路径

下面是一条兼顾面试、理论与实践的参考路线。

| 周次 | 学习内容 | 实践任务 |
|---|---|---|
| 1 | Alex Xu：需求分析、估算和答题框架 | 设计短链接系统 |
| 2 | Alex Xu：缓存、分区和消息队列 | 设计限流器 |
| 3 | DDIA：数据模型与存储 | 比较关系型、文档型和 KV 存储 |
| 4 | DDIA：复制与分区 | 设计多区域读写架构 |
| 5 | DDIA：事务、一致性与故障 | 分析强一致与最终一致方案 |
| 6 | DDIA：批处理与流处理 | 设计日志分析流水线 |
| 7 | Fundamentals of Software Architecture | 为现有项目写架构特性清单 |
| 8 | Software Architecture: The Hard Parts | 比较单体、模块化单体和微服务 |
| 9 | Building Microservices | 为一个业务域划分服务边界 |
| 10 | Release It! | 补充超时、重试、熔断和降级策略 |
| 11 | Google SRE | 为系统定义 SLI、SLO 与错误预算 |
| 12 | 综合复盘 | 完成一次 45 分钟系统设计 Mock |

---

## 系统设计检查清单

完成一个系统设计时，可以按以下顺序检查。

### 1. 需求

- 核心用户场景是什么？
- 哪些功能明确不在范围内？
- 延迟、可用性、一致性和成本目标是什么？

### 2. 规模估算

- 日活、峰值 QPS 和读写比例是多少？
- 单条数据大小和保留周期是多少？
- 网络、存储与计算资源大致需要多少？

### 3. 接口与数据

- 核心 API 是什么？
- 数据模型如何表达主要实体和关系？
- 哪些操作必须幂等？

### 4. 高层架构

- 请求从入口到存储经过哪些组件？
- 哪些流程同步，哪些流程异步？
- 系统的信任边界和故障边界在哪里？

### 5. 深入设计

- 如何分区、复制和缓存？
- 如何处理热点、重复消息和乱序事件？
- 一致性模型是什么？
- 扩容和数据迁移如何进行？

### 6. 可靠性

- 超时、重试和熔断策略是什么？
- 单个依赖失效时系统如何降级？
- 如何限流、削峰和施加背压？
- RPO、RTO 和容灾策略是什么？

### 7. 可观测性与运维

- 核心 SLI 和 SLO 是什么？
- 哪些指标需要告警？
- 如何追踪一次跨服务请求？
- 如何安全发布和快速回滚？

### 8. 权衡

- 当前方案优化了什么？
- 它牺牲了什么？
- 在什么条件下需要重新设计？

---

## 阅读笔记模板

可以为每本书建立一个独立笔记文件：

```markdown
# 书名

## Why I Read It

我为什么读这本书？

## Key Ideas

- 
- 
- 

## Important Trade-offs

| 方案 | 优势 | 代价 | 适用场景 |
|---|---|---|---|
| | | | |

## One Design I Would Change

读完之后，我会如何改进一个做过的系统？

## Questions

- 还有哪些问题没有想明白？
- 哪些观点需要通过实验或实践验证？
```

---

## 最后

系统设计能力通常来自三件事：

1. **阅读原理**，知道系统为什么会失败；
2. **分析真实系统**，观察不同团队如何做取舍；
3. **持续练习表达**，把复杂设计讲得清楚、具体且可验证。

书单只是地图。真正的进步来自不断设计、复盘和修正。

<p align="right"><a href="./README.md">← Back to reading archive</a></p>

---

<div align="center">

### Design for change. Prepare for failure.

<sub>A living reading guide · Updated along the way</sub>

</div>
