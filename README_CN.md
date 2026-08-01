# OrthoReg-World

面向自适应混合现实骨科配准的影像驱动在线世界模型

[English](README.md) · [流程演示视频](https://youtu.be/YVuVoCD0BBM) · [下载公开元数据](data/TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip)

![Status](https://img.shields.io/badge/status-research%20prototype-6f42c1)
![Public data](https://img.shields.io/badge/public%20data-18%20Adaptive%20sessions-0b7fab)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)

<p align="center">
  <a href="https://youtu.be/YVuVoCD0BBM">
    <img src="assets/demo-overview.jpg" alt="OrthoReg-World 在 Apple Vision Pro 上的流程演示" width="900">
  </a>
</p>

<p align="center">
  <a href="https://youtu.be/YVuVoCD0BBM"><strong>▶ 在 YouTube 播放完整流程视频</strong></a>
</p>

> GitHub README 不支持直接嵌入 YouTube 播放器，因此点击预览图或播放链接后会进入 YouTube。

## 项目简介

OrthoReg-World 是一个运行于 Apple Vision Pro 的自适应混合现实骨科配准研究原型。系统维护影像驱动的在线世界模型，在采集过程中持续评估配准质量，并判断当前观测证据是否已经充分。演示视频展示了股骨和胫骨配准，以及全膝关节置换术截骨平面的可视化。

本仓库用于公开项目介绍和数据。Enterprise API 集成、应用源代码、部署凭据、原始相机图像以及患者数据均不在公开范围内。

## 与论文一致的实验说明

论文报告了两个相关但彼此独立的研究，两者的样本范围不能合并表述。

### 前瞻性 Adaptive stop-and-complete 研究

- 18 次使用 Adaptive 协议的真实 HMD 采集会话。
- 本仓库的公开 ZIP 包含这 18 个会话的去标识化、非像素元数据。
- 审计记录保留原始 QC 信息，包括两个会话中的重复或测量无效 TRE 记录。

### Adaptive 与 Fixed 的受约束随机化比较

- 36 个正式 runs：Adaptive 18 个，Fixed-k=10 18 个。
- 覆盖 3 名操作者、2 台 Vision Pro、股骨与胫骨，以及 3 组独立目标点布局。
- 在采集开始前，预先冻结的受约束随机化方案为每个 operator–device–anatomy–layout cell 分配一个协议。
- 每个 run 使用 7 个独立目标点，共分析 252 个 held-out target errors。

预先规定的 run-level 终点是 7 个目标点的目标配准误差均方根（**TRE RMSE**），不是点云 RMSE，也不是其他配准残差。

| 论文结果 | Adaptive | Fixed-k=10 |
| --- | ---: | ---: |
| Runs | 18 | 18 |
| 平均 TRE RMSE | 1.01 ± 0.11 mm | 2.46 ± 0.44 mm |
| 7 个目标点全部 ≤ 3 mm 的 runs | 18/18 | 3/18 |

校正后的 Adaptive-minus-Fixed 差值为 **−1.45 mm**，HC3 95% 置信区间为 **−1.68 至 −1.22 mm**。

以上是论文报告的比较结果。可下载 ZIP 是另一个 18-session Adaptive 元数据补充包，其中**不包含** Fixed-k 比较数据包或受约束随机化方案。详见[论文与公开数据对应关系](docs/manuscript-data-alignment.md)。

## 公开元数据包

[下载 `TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip`](data/TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip)

该数据包包含 18 个正式 Adaptive 会话的去标识化元数据、审计表、分析支持表、数据结构说明、校验和以及非像素内容验证脚本。

| 数据包属性 | 数值 |
| --- | ---: |
| 真实采集会话 | 18 |
| 协议 | 仅 Adaptive |
| 解压后的文件数 | 967 |
| 原始图像、视频、深度、截图或像素数据 | 无 |
| 源数据中的设备编号 | 不可用（`NA`） |

### 终点数据的重要说明

数据包保留了与源数据一致的原始审计记录，因此原始 session summary 的 TRE 字段可能包含重复或测量无效的观测。复现论文口径的 session endpoint 时，应使用 analysis-support 表中“每个目标点最新且唯一的有效观测”字段，并保留随附的 QC 标记。不要静默删除原始审计记录，也不要把已标记的原始 summary 数值直接当作最终终点。

### 下载后验证

在仓库根目录运行：

```bash
shasum -a 256 -c MANIFEST_SHA256.txt
unzip data/TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip
cd TMI_OrthoRegWorld_Online_Adaptive_Metadata
python3 scripts/verify_no_frames.py . --expected-sessions 18
```

数据包内的验证脚本会检查 manifest、会话数量、校验和清单，并确认不存在帧图像或其他像素数据。

## 仓库结构

```text
OrthoReg-World/
├── README.md
├── README_CN.md
├── LICENSE
├── MANIFEST_SHA256.txt
├── SECURITY.md
├── assets/
│   └── demo-overview.jpg
├── data/
│   ├── README.md
│   └── TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip
└── docs/
    ├── data-availability-statement.txt
    └── manuscript-data-alignment.md
```

## 使用范围与限制

OrthoReg-World 是在受控 phantom 实验中评估的研究原型，不是医疗器械，未经批准用于临床决策，不能用于患者诊疗。公开元数据不包含私有应用代码或受许可限制的 Enterprise 服务。

## 引用

在正式出版信息可用前，可按以下方式引用：

```text
Jiang K, Fan W, Shi H, Hu L, Lin Z, Zeng B, Chen X.
OrthoReg-World: An Imaging-Grounded Online World Model for Adaptive
Mixed-Reality Orthopedic Registration. Research project and public
metadata supplement, 2026.
https://github.com/K1mjiang/OrthoReg-World
```

## 许可证

本仓库公开材料与元数据补充包采用 [Creative Commons Attribution 4.0 International License](LICENSE)。第三方软件、服务和商标仍受各自条款约束。
