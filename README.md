# 🚀 Aider-TUI: The Professional AI Pair Programming Shell

**Aider-TUI** 是基于 Aider 开发的增强型终端界面。它通过重构底层的交互逻辑，解决了原生界面光标抖动、大项目路径遮挡以及误触发送等痛点，为你提供如 IDE 般稳定的终端开发体验。

---

<p align="center">
Aider-TUI lets you pair program with LLMs to start a new project or build on your existing codebase. 
</p>

<p align="center">
  <img
    src="https://nanshaws.top/wp-content/uploads/2026/01/demo.gif"
    alt="aider-tui screencast"
  >
</p>

<p align="center">
  <img
    src="https://nanshaws.top/wp-content/uploads/2026/01/demo01.gif"
    alt="aider-tui screencast"
  >
</p>

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

---

## 🛠️ 安装与快速开始

### 1. 克隆并安装
记住一定要将配置文件.env.example重命名为.env
```bash
git clone https://github.com/nanshaws/Aider-TUI.git
cd aider-tui
mv .env.example .env
python -m pip install --upgrade pip
pip install -e .
pip install playwright
playwright install chromium
```

### 2. 🚀 启动与使用指南

安装完成后，你可以在终端通过 `aider-tui` 命令直接启动。

### 🔑 全局一键配置 (Aider-TUI 独有)

不同于原版需要反复设置环境变量，**Aider-TUI** 支持在安装目录配置全局 `.env`。

1. **进入安装目录**，找到 `.env` 文件。
2. **填入你的万能配置**（以阿里云/OpenAI兼容模式为例）：
```bash
# 设置默认启动模型，从此无需再加 --model 参数
AIDER_MODEL=openai/qwen-long-latest

# 配置 OpenAI 兼容格式的 Base URL 和 Key
OPENAI_API_BASE=[https://dashscope.aliyuncs.com/compatible-mode/v1](https://dashscope.aliyuncs.com/compatible-mode/v1)
OPENAI_API_KEY=sk-xxxx...
```

![image-20260113153740657](https://nanshaws.top/wp-content/uploads/2026/01/image-20260113153740657.png)

**保存并运行**：现在你在任何项目目录下输入 `aider-tui`，它都会自动加载这套配置。

![image-20260113151550821](https://nanshaws.top/wp-content/uploads/2026/01/image-20260113151550821.png)

```bash
cd  项目目录
# 使用默认模型 （如果设置了环境变量，就直接使用环境变量里面的）
aider-tui

# 使用 Gemini 3 Pro 预览版 (代码内置别名)
aider-tui --model gemini

# 使用 DeepSeek Chat (代码内置别名)
aider-tui --model deepseek

# 使用 Gemini 2.5 Flash (代码内置别名)
aider-tui --model flash
```

| **模型别名** | **实际模型路径**              | **需设置的环境变量** | **获取渠道**                                        |
| ------------ | ----------------------------- | -------------------- | --------------------------------------------------- |
| `gemini`     | `gemini/gemini-3-pro-preview` | `GEMINI_API_KEY`     | [Google AI Studio](https://aistudio.google.com/)    |
| `flash`      | `gemini/gemini-2.5-flash`     | `GEMINI_API_KEY`     | [Google AI Studio](https://aistudio.google.com/)    |
| `deepseek`   | `deepseek/deepseek-chat`      | `DEEPSEEK_API_KEY`   | [DeepSeek Platform](https://platform.deepseek.com/) |
| `r1`         | `deepseek/deepseek-reasoner`  | `DEEPSEEK_API_KEY`   | [DeepSeek Platform](https://platform.deepseek.com/) |

### 3. 🛠️ 常用指令

| **命令**                 | **作用**                                                     |
| ------------------------ | ------------------------------------------------------------ |
| `/add <文件名>`          | 将文件加入对话（文件名会立即出现在输入框上方的预览区）       |
| `/ls`                    | 列出当前仓库中所有可用的文件                                 |
| `/drop <文件名>`         | 从对话中移除文件                                             |
| `/exit`                  | 退出 Aider-TUI                                               |
| `/open` <网站名字>       | Launch any URL in your browser instantly.                    |
| `/screenshot` <网站名字> | The AI can now request or perform background screenshots of your web apps. |

## 📊 对比原生 Aider

| **特性**     | **原生 Aider**   | **Aider-TUI (Yours)**     |
| ------------ | ---------------- | ------------------------- |
| **输入重心** | 随文件名路径变动 | **始终固定在左下方**      |
| **回车行为** | 容易误触发发送   | **智能判断符号平衡**      |
| **视觉排版** | 简单的字符串堆叠 | **Rich 驱动的列式分层**   |
| **提示引导** | 较少             | **底部 Toolbar 实时引导** |

------

### 🔄 从 Aider 到 Aider-TUI 的进化清单

- **真正的 TUI 体验**：
  - 将输入框标志由 `AIDER` 修改为 `AIDER-TUI`。
  - 重构了交互重心，无论你的项目路径多深，输入框永远在左下角等你。
  
- **全局“能源中心”**：
  - 通过硬核修改 `main.py`，现在你只需在 Aider-TUI 安装目录下配置一次 `.env`，全系统的任何代码文件夹都能直接调用这些 Key。
  
- **不丢包的仓库图谱**：
  - 我们修复了社区普遍存在的 `repomap.py` 报错问题，完美支持最新的 `tree-sitter` 解析，不再因为依赖更新而崩溃。
  
- **极简启动指令**：
  - 重新定义了 `pyproject.toml`，现在只需输入 `aider-tui --model g3` 即可瞬间唤醒经过 Architect 模式优化的 Gemini 3。
  
  ### 🌈 Visual Feedback Loop (New!)
  
  Aider-TUI is no longer blind. It can now interact with the web directly:
  
  - **`/open`**: Launch any URL in your browser instantly.
  - **`/screenshot`**: The AI can now request or perform background screenshots of your web apps.
  - **Vision-Link**: Combine with multi-modal models (GPT-4o, Gemini, Qwen-VL) to let the AI "see" UI bugs and fix them autonomously.

## 🤝 贡献与感谢

本项目基于 [Aider](https://github.com/Aider-AI/aider) 开发，感谢原作者提供的卓越基础。

如果你喜欢这套更人性化的 TUI 逻辑，欢迎提交 Issue 或 PR！