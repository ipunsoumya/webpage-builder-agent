# Webpage Builder Agent

A multi-agent pipeline, built on [Google's Agent Development Kit (ADK)](https://github.com/google/adk-python), that turns a plain-language description of a webpage into a single, production-ready HTML file. A sequential team of LLM agents — a Business Analyst, a Visual Designer, and a Front-End Developer — collaborate to plan, design, and generate the final page.

## How It Works

The `orchestrator_agent` runs three sub-agents in strict sequence, passing structured Markdown output from one agent to the next via shared session state:

1. **Requirement Writer Agent** (`agents/requirement_writer`)
   Acts as a Business Analyst/UX Strategist. Converts raw user input into a detailed Markdown **Requirement Specification Document** (project overview, information architecture, core features, design guidelines, content requirements), enforcing a minimalist, sleek design philosophy.

2. **Designer Agent** (`agents/designer`)
   Acts as a Visual Architect. Reads the requirements (`state['requirement_writer_output']`) and produces a precise **Visual Design & Layout Blueprint** in Markdown — color tokens, typography, spacing scale, section-by-section layout, and interaction/animation specs.

3. **Code Writer Agent** (`agents/code_writer`)
   Acts as a Front-End Developer. Reads both the requirements and the design blueprint (`state['requirement_writer_output']`, `state['designer_output']`) and generates a single, responsive HTML5 file (embedded CSS/JS, semantic markup, CSS variables). It uses the `write_to_file` tool to save the result — it never returns raw HTML as chat output.

Each agent's persona, rules, and Markdown output template are defined in its `instructions.txt`, with a short `description.txt` summarizing its role for the orchestrator.

## Project Structure

```
webpage-builder-agent/
├── agents/
│   ├── orchestrator_agent/   # SequentialAgent wiring the pipeline together
│   ├── requirement_writer/   # Business Analyst agent (requirements -> Markdown)
│   ├── designer/              # Visual Architect agent (requirements -> design blueprint)
│   └── code_writer/          # Front-End Developer agent (design -> final HTML)
├── tools/
│   └── file_writer.py        # Tool used by the Code Writer agent to save output
├── utils/
│   └── load_file.py          # Helper to load instructions/description text files
├── output/                   # Generated HTML pages are written here (git-ignored)
├── main.py                   # Placeholder entry point
├── pyproject.toml            # Project metadata & dependencies
└── uv.lock                   # Locked dependency versions (uv)
```

## Prerequisites

* Python >= 3.11
* [uv](https://docs.astral.sh/uv/) (recommended) or `pip`
* A Google API key with access to the Gemini models (e.g., `gemini-3.5-flash`)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ipunsoumya/webpage-builder-agent.git
   cd webpage-builder-agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```
   or, using pip:
   ```bash
   pip install -e .
   ```

3. **Configure your API key**
   Create a `.env` file inside `agents/` with your Google API credentials:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```

## Usage

Run the orchestrator agent through the ADK CLI (from the repository root):

```bash
adk run agents/orchestrator_agent
```

Or launch the ADK web UI for an interactive chat session:

```bash
adk web agents
```

Describe the webpage you want (e.g., *"a minimalist portfolio site for a photographer with a hero section, gallery, and contact form"*), and the pipeline will:

1. Draft a requirement specification.
2. Produce a visual design blueprint.
3. Generate and save a complete HTML file to `output/<timestamp>_generated_page.html`.

## Output

Generated pages are self-contained HTML5 documents — CSS lives in a `<style>` block and JavaScript in a `<script>` block, with no external dependencies beyond optional font/icon CDNs. Files are saved under `output/`, which is git-ignored.

## Tech Stack

* [Google ADK](https://github.com/google/adk-python) — multi-agent orchestration (`SequentialAgent`, `LlmAgent`)
* Gemini (`gemini-3.5-flash`) — underlying LLM for each agent
* Python 3.11+

## License

No license specified yet.