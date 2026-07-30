# OrthoReg-World

基于 Apple Vision Pro 的混合现实骨科配准与 TKA 导航研究

[English](README.md)

[![OrthoReg 混合现实 TKA 导航演示](assets/demo-overview.jpg)](https://youtu.be/YVuVoCD0BBM)

## 项目简介

**OrthoReg-World** 是一个运行于 Apple Vision Pro 的混合现实骨科导航科研原型。
当前演示流程包括胫骨配准、股骨配准，以及在统一空间坐标环境中显示规划的虚拟
TKA 截骨平面。

本仓库作为项目的公开 GitHub 首页与实验数据发布仓库，与私有主程序仓库完全
分离。实验均在骨科 phantom 上完成，不涉及患者或真实手术。

## 视频演示

视频展示以下流程：

1. 胫骨空间配准；
2. 股骨空间配准；
3. 已配准解剖模型的空间显示；
4. 虚拟 TKA 截骨平面显示。

▶ **[在 YouTube 观看完整演示](https://youtu.be/YVuVoCD0BBM)**

## 本仓库公开的内容

- 项目目的与高层工作流程
- Vision Pro phantom 演示画面
- 脱敏后的 run 级与 TRE 点级实验数据
- 公开工作流事件和质量警告汇总
- 数据字典、匿名设备映射及分析结果
- 不依赖第三方库的数据验证脚本

## 不公开的内容

- Vision Pro 主程序完整源码
- 专有配准和导航模块
- Enterprise API 集成及服务实现细节
- 凭据、内部端点、设备序列号和私有日志
- 未公开模型、开发数据及内部评估材料
- 尚未完成逐帧隐私审查的原始图像和视频导出

## 开放实验数据

公开数据来自一项前瞻性、平衡的 phantom 对照实验。

| 项目 | 公开数据 |
| --- | ---: |
| 正式完成的 runs | 36 |
| Adaptive / Fixed k=10 | 18 / 18 |
| 匿名操作者 | 3 |
| 匿名 Vision Pro 设备 | 2 |
| 解剖结构 | Tibia 与 Femur |
| Held-out TRE groups | 3 |
| 每次 run 的 held-out TRE 点 | 7 |
| TRE 点级记录总数 | 252 |

该实验没有随机分配记录，因此只能表述为“前瞻性、平衡对照”，不能表述为
随机试验。主分析单位是一次完整 run，不得将252个TRE点视为252次独立实验。

### Phantom 主要结果

| Run级结果 | Adaptive (n=18) | Fixed k=10 (n=18) |
| --- | ---: | ---: |
| TRE RMSE，均值 ± SD | 1.008 ± 0.111 mm | 2.458 ± 0.438 mm |
| 7个TRE点全部≤3 mm | 18/18 | 3/18 |
| 配准采集时间，均值 | 54.2 s | 23.3 s |

校正后的 Adaptive-minus-Fixed TRE RMSE 估计值为 **−1.450 mm**，HC3 95%
置信区间为 **−1.682至−1.218 mm**。这些数据支持在当前 phantom 与实验协议
下的精度和可靠性差异，但不支持速度优势，也不能外推为临床有效性或患者安全性。

完整口径见 [`docs/open-data-summary.md`](docs/open-data-summary.md)，字段定义见
[`metadata/data_dictionary.csv`](metadata/data_dictionary.csv)。

## 数据验证

```bash
python3 scripts/validate_open_data.py
```

验证脚本会检查文件和行数、唯一标识符、实验分层平衡、每次run的7个TRE点、
跨表覆盖、重复记录、公开统计结果一致性，以及常见敏感信息模式。

公开的工作流事件表为保持与源导出一致，保留了1条完全重复的规划事件。如果进行
事件频次分析，应先按整行进行去重。

## 开源边界

公开数据中使用 `OP-01` 至 `OP-03` 表示匿名操作者，使用 `VP-A` 和 `VP-B`
表示匿名设备，不发布硬件序列号。原始实验压缩包及视觉帧不进入本仓库。

本仓库中的公开实验数据、文档、分析结果、演示图片和验证代码采用
[Creative Commons Attribution 4.0 International](LICENSE) 许可证。复用时应注明
“OrthoReg-World project and 36-run phantom comparison dataset”，链接至本仓库和
CC BY 4.0 许可证，并说明是否进行过修改。

该许可证不适用于未进入本仓库的 OrthoReg 私有主程序、Enterprise API 集成、
专有模块、原始导出或其他非公开材料。

## 免责声明

OrthoReg-World 仅用于科研与工程验证，不得用于诊断、治疗、手术规划或真实术中
导航。公开的 phantom 实验结果不构成患者安全性、临床疗效或监管批准证明。

Apple Vision Pro 是 Apple Inc. 的商标。本独立研究项目与 Apple 无附属关系，
亦未获得 Apple 背书。
