# 神笔马良 · Shen Bi Ma Liang

[![Validate](https://github.com/Ysx12138/shen-bi-ma-liang/actions/workflows/validate.yml/badge.svg)](https://github.com/Ysx12138/shen-bi-ma-liang/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An agent-agnostic workflow package for composing original Web and mobile UI atmosphere images from a structural design spec and visual-reference attributes.

[中文](#中文) · [English](#english) · [Agent compatibility](#agent-compatibility) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changelog](CHANGELOG.md)

## 中文

一个可被不同 AI 编程/工作流 Agent 使用的原创 Web / Mobile UI 氛围图工作流；Codex 只是其中一个带原生入口的适配平台。

它不把参考图直接交给最终生图模型去“照着画”，而是先把输入拆成可审阅的规则，再组合成一张新的 UI 氛围图：

```text
design.md → A（结构）
reference images → U（界面组织）/ C（色彩与材质）/ M（内容与氛围）
A + U + C + M → Mix spec → original UI atmosphere image
```

## 它解决什么

常规的“参考图混合”很容易变成两种结果：要么贴近某一张图，要么掉进模型惯用的 SaaS 模板。神笔马良把来源拆开后再重新编译：

- `A` 只控制结构：层级、字感、间距、形状和组件关系。
- `U` 只控制界面组织：信息顺序、导航、控件语法和密度。
- `C` 是唯一的色彩与材质主控。
- `M` 只控制产品内容、氛围与视觉焦点。

批量模式会让三张参考图轮换承担 `U / C / M`，并记录组合历史，尽量避免下一批又撞回同一种组合。

### 选择机制：不是随便抽三次

设本轮结构主控为 `A`，参考候选集合为 `R`。先从 `R` 中抽取三个互不相同的来源 `{R1, R2, R3}`，再从下面两组**平衡排列**中随机选一组：

| 组别 | Mix 01 | Mix 02 | Mix 03 |
| --- | --- | --- | --- |
| A 组 | `U1-C2-M3` | `U2-C3-M1` | `U3-C1-M2` |
| B 组 | `U1-C3-M2` | `U3-C2-M1` | `U2-C1-M3` |

这不是从六种排列里任意抽三种。每一组都构成一个 3×3 的拉丁方阵式轮换：在三个 Mix 中，每张参考图恰好各做一次 `U`、一次 `C`、一次 `M`，并且单个 Mix 内的 `A / U / C / M` 来源必须全不相同。于是，角色使用是均匀的，三张图不会都在同一个维度上反复发力。

跨批次的去重键是：

```text
signature = (A 的稳定来源 ID, sort({R1, R2, R3}) 的稳定来源 ID)
```

`A` 可以在未来再次被抽中；限制的不是 `A` 本身，而是同一个 `A` 不能再配到同一组三张参考图。若有 `n` 张合格参考图可供某个 `A` 使用，最多有 `C(n, 3)` 组互异三元组合可探索。即使换一组角色排列，也不会复用已登记的同一个签名——这样优先保证“来源集合不同”，而不只是把同一批素材重新洗牌。

为避免生成结果只有“精致但空”的 AI 界面，中文工作流额外要求每张成图都有一个承担视觉重量的真实感实体锚点：人物、实体物体 / 材质 / 产品，或环境 / 场景。它不是装饰素材，而需要和内容层级、裁切和界面任务一起被编译进提示词。

## 输出约束

- Web：一张完整页面，带有来自 `C-spec` 的背景承托和清楚的页面边界；不是满版白色截图。
- Mobile：先锁定一个已批准的设备 / 面板版式，再生成；参考图不能临时改变版式。
- 不复制 Logo、品牌、原图人物 / 物体 / 照片或完整布局。
- 每个保留图片都可登记一条专属的 blended-reference prompt，供后续运营平台把图片和文字参考一起上传。

### 可插拔生图模型

生成前的 A/U/C/M 抽取、组合、审核与文件契约不依赖任何一家模型；只有最后“把已编译的 prompt 渲染成图片”这一步可以换模型。仓库提供统一的本机路由配置，不保存 API Key：

```bash
# 查看可选路由
python3 scripts/configure_image_provider.py list

# 让当前 Agent 使用它自身已配置的生图工具
python3 scripts/configure_image_provider.py use agent-native

# 配置外部服务；模型 ID 由使用者填写，避免仓库把会变动的型号写死
python3 scripts/configure_image_provider.py use openai-images-api --model <model-id>
python3 scripts/configure_image_provider.py use google-genai-api --model <model-id>
python3 scripts/configure_image_provider.py use stability-api --model <model-id>
python3 scripts/configure_image_provider.py use replicate-api --model <model-id>
python3 scripts/configure_image_provider.py use fal-api --model <model-id>
python3 scripts/configure_image_provider.py use comfyui-http --model <workflow-or-model-id>
```

命令会把非敏感配置写入 `user-config/image-generation-provider.json`，它已被 Git 忽略。不同 Agent 都读取同一份文件，再按自己的原生工具、已授权 HTTP/API 能力或本地 ComfyUI 能力执行；若当前 Agent 没有相应工具或凭据，必须说明并保留 prompt/artifact，不能假装已生成或暗中换模型。完整字段和边界见 [providers/README.md](providers/README.md)。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | Codex 实际加载入口（英文） |
| [SKILL.zh-CN.md](SKILL.zh-CN.md) | 中文审阅与设计说明 |
| [references/final-output-templates.md](references/final-output-templates.md) | 已批准的 Web / Mobile 输出模板 |
| [assets/design-template.md](assets/design-template.md) | `design.md` 的起始模板 |

## 使用

选择下方与你的 Agent 对应的入口，将本仓库保持在 Agent 可读取的项目或本地规则目录；然后提供：

1. 一份用于结构约束的 `design.md`；
2. 一张或多张视觉参考；
3. 产品任务、目标设备和输出数量。

工作流会在 `inspiration-runs/` 下保存本轮的参考 spec、Mix spec、提示词、输出和审核记录。该目录是运行产物，不包含在本仓库中。

### 登记默认素材目录

如果你已经把参考图和 `design.md` 整理好，可以明确告诉 Skill 素材根目录、设计文件（或设计规范目录）和可选的参考图目录。它会校验路径后，在本机保存默认值；以后没有另行指定时，就从这个位置寻找素材，并把运行记录放到该根目录下的 `inspiration-runs/`。

这份设置保存在 `user-config/default-materials-root.md`，被 Git 忽略：它不会被推送到公开仓库，也可以被明确更新或清除。

## 关于素材与边界

本项目只公开工作流和提示词约束，不包含参考图、生成结果或运营平台资料。设计时使用的视觉素材来自 AI 生成，但工作流仍要求每一轮生成使用新的原创内容，并避免复制来源中的品牌、文案、人物、物体、照片或完整布局。

## English

Shen Bi Ma Liang is an agent-agnostic workflow package for producing original, non-runnable UI atmosphere images. Codex has a native Skill entry, while other agents use the same portable core instructions. Rather than passing visual references straight to an image model, the workflow extracts and compiles four bounded inputs:

```text
design.md → A (structure)
reference images → U (UI organization) / C (color and material) / M (content and atmosphere)
A + U + C + M → Mix spec → original UI atmosphere image
```

`A` sets hierarchy and layout character, `U` sets information grammar, `C` is the sole color/material authority, and `M` sets content and visual emphasis. Controlled batches rotate three references across U/C/M and preserve combination history to avoid repeating the same source set.

### Selection mathematics

For structural master `A`, choose a distinct reference triple `{R1, R2, R3}` from the eligible reference set `R`, then select one of two balanced permutation groups:

| Group | Mix 01 | Mix 02 | Mix 03 |
| --- | --- | --- | --- |
| A | `U1-C2-M3` | `U2-C3-M1` | `U3-C1-M2` |
| B | `U1-C3-M2` | `U3-C2-M1` | `U2-C1-M3` |

Each group is a 3×3 Latin-square-style rotation: across the three mixes, every reference takes `U`, `C`, and `M` exactly once, while the sources assigned to `A`, `U`, `C`, and `M` inside any individual mix must all differ. The workflow therefore never picks an arbitrary three from six permutations.

Cross-run uniqueness uses `signature = (stable_id(A), sort({stable_id(R1), stable_id(R2), stable_id(R3)}))`. `A` may recur in a later batch, but never with the same unordered reference triple unless the user explicitly authorizes reuse. With `n` eligible references for a fixed `A`, the pool contains `C(n, 3)` distinct source triples. The history deduplicates source triples even if a different role group would otherwise be available, prioritizing real material diversity over a superficial reshuffle.

### Install and use

1. Clone or download this repository somewhere your agent can read.
2. Load the platform adapter listed below, or load the portable [AGENTS.md](AGENTS.md) directly.
3. Give the agent a structural `design.md`, one or more visual references, a product brief, target device, and output count.

The Skill writes an auditable run folder with reference specs, compiled mix specs, prompts, output files, and review notes. Runtime artifacts, user-local default paths, source images, and generated images are intentionally ignored by Git.

## Agent compatibility

The workflow contract is platform-neutral: it specifies files, decisions, constraints, and output artifacts rather than a proprietary tool call. Use [AGENTS.md](AGENTS.md) as the canonical portable entry; choose a thin adapter only to match your agent's loading convention.

| Agent | Entry | How to use it |
| --- | --- | --- |
| Codex | [SKILL.md](SKILL.md) | Install this repository as a local Codex Skill. `agents/openai.yaml` supplies the Codex UI metadata. |
| Claude Code | [adapters/claude-code/CLAUDE.md](adapters/claude-code/CLAUDE.md) | Add or import this bridge from a project/user `CLAUDE.md`, with the repository available to read. |
| Gemini CLI | [adapters/gemini-cli/GEMINI.md](adapters/gemini-cli/GEMINI.md) | Add or import this bridge from a project/user `GEMINI.md`, with the repository available to read. |
| Cursor | [adapters/cursor/shen-bi-ma-liang.mdc](adapters/cursor/shen-bi-ma-liang.mdc) | Copy it into `.cursor/rules/` and keep the repository available to the workspace. |
| Other agents | [AGENTS.md](AGENTS.md) | Give the agent this file and the referenced templates; no provider-specific API is required. |

The adapters must not alter the A/U/C/M selection mathematics, direct-reference boundary, locked output-template rules, review contract, or local-only path handling. They only tell a platform where to begin reading.

## Pluggable image-model routing

The A/U/C/M extraction, mixing, review, and artifact contract are model-independent. Only the final rendering step is routed. Configure a local, Git-ignored provider record with one command:

```bash
python3 scripts/configure_image_provider.py list
python3 scripts/configure_image_provider.py use agent-native
python3 scripts/configure_image_provider.py use openai-images-api --model <model-id>
python3 scripts/configure_image_provider.py use comfyui-http --model <workflow-or-model-id>
```

Supported routes include the current agent's native image tool, OpenAI-style image APIs, Google GenAI APIs, Stability APIs, Replicate, fal, local ComfyUI HTTP, and a custom HTTP adapter. The command writes `user-config/image-generation-provider.json` without an API key; the provider's credential is referenced only by environment-variable name. Every supported agent reads the same routing record, then uses its own available tool or authorized client to render the already compiled prompt.

Provider routing may change the renderer, not the workflow: do not use it to skip reference-spec extraction, pass raw references by default, relax a locked layout, replace a required review artifact, or silently fall back to a different model. Read [providers/README.md](providers/README.md) for the configuration schema and handoff rules.

### Project boundaries

- This repository contains workflow instructions and templates, not reference images or generated assets.
- References are analyzed as evidence; the default workflow does not send raw reference images to final generation.
- Do not copy source brands, copy, logos, people, photographs, products, or full layouts.
- This project is released under the [MIT License](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Verification

Run the repository validation locally with:

```bash
python3 scripts/validate_skill.py
```

GitHub Actions runs the same check on pushes and pull requests.

## Community

- Report reproducible defects through [GitHub Issues](https://github.com/Ysx12138/shen-bi-ma-liang/issues).
- Discuss workflows, examples, or ideas in [GitHub Discussions](https://github.com/Ysx12138/shen-bi-ma-liang/discussions).
- Read [SUPPORT.md](SUPPORT.md), [SECURITY.md](SECURITY.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for the appropriate channel and expectations.

---

`神笔马良` 是一个作品名：它关注的不是把一张图描得更像，而是把一组视觉线索拆开、重组，再画出一张能真正被继续使用的图。
