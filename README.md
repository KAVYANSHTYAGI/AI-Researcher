# AI-Researcher

# Autonomous Multi-Agent AI Research Lab

---

**Revolutionize AI/ML research with a fully autonomous, agent-driven local system**  
_Beat benchmarks. Invent new models. Automate experiments. All with minimal human oversight._

---

## 🚀 Project Overview

The Autonomous Multi-Agent AI Research Lab is a modular, locally running, next-generation research platform that combines the **creativity and intelligence of LLMs** with rigorous, automated experiment orchestration.  
It enables research teams, organizations, or solo researchers to rapidly:

- Generate **novel research ideas**
- Autonomously write and debug code
- Run and track experiments safely
- Evaluate results and produce publication-ready reports

All of this is managed by specialized AI agents, with robust approval and correction workflows, and full resource management—**no constant human babysitting required**.

---

## 🧠 Core Features

- **Multi-Agent Architecture:** Specialized agents for creative ideation, code generation, experiment orchestration, and results evaluation.
- **Hybrid LLM Support:** Combine state-of-the-art cloud LLMs (e.g., GPT-4o via OpenAI API) with powerful local LLMs (e.g., Llama-3, DeepSeek Coder).
- **Robust Experiment Management:** All code, models, logs, and results are stored on disk—never lost, always reproducible.
- **Approval & Correction Loops:** Every big step is checked for ambiguity, errors, and benchmark alignment before proceeding.
- **Full Resource Safety:** Agents and experiments alternate GPU/CPU usage so resource conflicts are impossible.
- **Configurable, Extensible, Transparent:** All parameters, agents, and models are swappable via configs and modular code.

---

## 🏗️ Architecture & Workflow

### **System Agents**

| Agent           | Role                                                  | Model Example                    |
|-----------------|-------------------------------------------------------|----------------------------------|
| **Idea Agent**  | Proposes new research/model ideas; scans SOTA         | GPT-4o (API), Llama-3-70B        |
| **Manager Agent** | Reviews, approves, plans, enforces benchmarks       | Llama-3-8B, Mistral              |
| **Coder Agent** | Writes, debugs, and runs code for experiments         | DeepSeek Coder, CodeLlama, StarCoder-2, OpenDevin |
| **Reviewer Agent** | Evaluates results, visualizes, drafts reports      | Llama-3-8B, GPT-4o               |

### **High-Level Workflow**

1. **Prompt**: You enter a research goal (e.g., "Beat UNet on ACDC dataset").
2. **Ideation**: Idea Agent (cloud or local LLM) proposes a model or technique.
3. **Approval**: Manager Agent checks clarity, novelty, and feasibility.
4. **Development**: Coder Agent generates code, handles errors, and runs the experiment.
5. **Execution**: Experiment runs in isolation, freeing resources on completion.
6. **Review**: Reviewer Agent analyzes results, generates plots/reports, and recommends next steps.
7. **Iteration**: If needed, agents loop, retry, or escalate for human review.

**All actions, code, and results are stored on disk and tracked in memory for full transparency and safety.**

---

## 🗂️ Repo Structure

```plaintext
autonomous-research-lab/
│
├── agents/                  # Agent logic: idea, coder, manager, reviewer
│   ├── idea_agent.py
│   ├── coder_agent.py
│   ├── manager_agent.py
│   ├── reviewer_agent.py
│   └── __init__.py
│
├── llm_backends/            # LLM servers/wrappers: local (vLLM/LMDeploy) and cloud (OpenAI API)
│   ├── serve_llama.py
│   ├── serve_coder.py
│   ├── client.py
│   └── README.md
│
├── orchestrator/            # Main workflow control, scheduling, and agent task management
│   ├── scheduler.py
│   ├── task_queue.py
│   ├── process_manager.py
│   └── __init__.py
│
├── experiment/              # Handles experiment execution, logs, data, envs, results
│   ├── runner.py
│   ├── result_parser.py
│   ├── data_handler.py
│   ├── env_manager.py
│   ├── job_templates/
│   │   └── pytorch_train_template.py
│   └── __init__.py
│
├── memory/                  # Persistent experiment logs, agent memory, retrieval-augmented DB
│   ├── db.py
│   ├── vector_store.py
│   └── __init__.py
│
├── storage/                 # All experiment outputs: code, models, logs, results (disk-based)
│   ├── experiments/
│   └── .gitignore
│
├── configs/                 # YAML/JSON configs: agents, LLMs, experiments, datasets, workspace
│   ├── agents.yaml
│   ├── llm_servers.yaml
│   ├── experiment.yaml
│   ├── datasets.yaml
│   └── workspace.yaml
│
├── ui/                      # (Optional) Web dashboard or CLI interface
│   ├── web/
│   │   ├── app.py
│   ├── cli/
│   │   └── main.py
│   └── README.md
│
├── scripts/                 # Launch, clean, backup, and utility scripts
│   ├── launch_agents.sh
│   ├── run_experiment.sh
│   ├── clean_gpu.sh
│   ├── backup_db.sh
│   └── ...
│
├── tests/                   # Unit/integration tests for robustness and reliability
│   ├── test_agents.py
│   ├── test_runner.py
│   └── ...
│
├── requirements.txt         # Python dependencies
├── Dockerfile               # (Optional) For portable, reproducible deployment
├── README.md                # (You are here!)
└── LICENSE
