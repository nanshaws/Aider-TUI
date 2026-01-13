# 🚀 Aider-TUI: The Professional AI Pair Programming Shell

**Aider-TUI** 是基于 Aider 开发的增强型终端界面。它通过重构底层的交互逻辑，解决了原生界面光标抖动、大项目路径遮挡以及误触发送等痛点，为你提供如 IDE 般稳定的终端开发体验。

---

## ✨ 核心特性

### 1. 🔍 搜索框式交互设计 (Search-Box TUI)
不同于传统的 `>` 提示符，Aider-TUI 采用了**固定重心的搜索框 UI**：
* **视觉稳定性**：输入框始终固定在底部，不再随长路径文件名跳动。
* **信息分层显示**：上下文文件列表（Editable/Readonly）整齐排布在输入框上方，互不干扰。
* **动态状态栏**：底部状态栏实时显示快捷键提示与当前模型状态。

### 2. 🧠 结构化智能回车 (Structural Smart Enter)
再也不用担心代码写一半误触回车浪费 Token：
* **符号平衡校验**：自动检测 `{}`, `[]`, `()` 是否闭合。未闭合时回车自动换行。
* **分号终结符**：支持使用 `;` + `Enter` 明确表达提交意图。
* **智能识别**：自动识别 `/` 指令与确认操作，保持原生命令的高效性。

### 3. 🧪 深度优化模型支持
内置了针对 2026 年主流模型的最佳配置：
* **Gemini 3.0 Pro**: 完美适配 Architect 模式与超长上下文。
* **Qwen 2.5 Coder**: 针对国产最强编程模型优化的 `diff` 协议。
* **Reasoning Models**: 原生支持 QWQ 等推理模型的 `think` 标签过滤。

---

## 🛠️ 安装与快速开始

### 1. 克隆并安装
```bash
git clone https://github.com/nanshaws/Aider-TUI.git
cd aider-tui
pip install -e .
```

