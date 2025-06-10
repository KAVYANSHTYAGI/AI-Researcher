# AI-Researcher

# Autonomous Multi-Agent AI Research Lab

---

**Revolutionize AI/ML research with a fully autonomous, agent-driven local system**  
_Beat benchmarks. Invent new models. Automate experiments. All with minimal human oversight._

---

## 🚀 Project Overview
Project Overview

The Autonomous Multi-Agent AI Research Lab is a next-generation, locally running software system that transforms AI and ML research into an automated, agent-driven process.
It empowers researchers, teams, or organizations to rapidly generate new ideas, develop and debug code, manage experiments, and produce publication-ready results—with minimal human oversight.

This platform combines the creativity and expertise of Large Language Models (LLMs) with robust experiment orchestration, resource management, and clear safety controls.
It’s built for modularity, transparency, and enterprise-scale reliability.
Key Features

    Multi-agent architecture—specialized agents (Idea, Coder, Manager, Reviewer) for creativity, code writing, orchestration, and evaluation.

    Hybrid LLM support—combine local LLMs (for speed and privacy) with powerful cloud-based LLMs (like GPT-4o) for idea generation.

    Robust experiment management—run, track, and log every experiment and result, all data persisted to disk (not RAM).

    Approval and correction workflow—system checks every big decision, requests clarification or human approval as needed.

    Resource safety—GPU, CPU, and RAM usage are strategically controlled so heavy experiments never conflict with LLM inference.

    Extensible and transparent—modular structure and detailed logging make extension and auditing easy.

How It Works
Agents & Their Roles

    Idea Agent:

        Generates new research ideas, architecture tweaks, and experimental directions.

        Uses the most creative LLM available (e.g., GPT-4o via cloud, or local Llama-3-70B).

        Reads benchmarks, suggests how to beat SOTA, and provides concrete proposals.

    Manager Agent:

        The “conductor” of the system.

        Checks ideas for clarity and feasibility, requests more detail if needed.

        Approves or rejects plans, monitors progress, and enforces goals/benchmarks.

        Decides when to loop, retry, ask for clarification, or escalate for human approval.

    Coder Agent:

        Turns approved ideas into runnable, real code.

        Uses specialized code LLMs (DeepSeek Coder, CodeLlama, StarCoder-2, OpenDevin) running locally.

        Handles debugging, code improvement, and error correction through repeated attempts.

        Manages code execution and interacts with experiment runner.

    Reviewer Agent:

        Analyzes and validates results from each experiment.

        Generates visualizations, metrics, and publication-ready summaries or drafts.

        Detects suspicious results (e.g., hallucination, anomalies) and flags for review.

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
├── agents/                  
│   ├── idea_agent.py        # Handles querying GPT-4o API for new research ideas; includes prompt engineering and response parsing
│   ├── coder_agent.py       # Interfaces with local code LLMs (e.g., DeepSeek Coder, CodeLlama) to write, edit, debug code; manages retries and error handling
│   ├── manager_agent.py     # Orchestrates workflow, approval logic, enforces benchmarks, checks for ambiguity, halts or loops as needed
│   ├── reviewer_agent.py    # Evaluates results, generates reports/visualizations, detects hallucinations, drafts paper summaries
│   └── __init__.py          # Initializes the agents module; enables easy imports
│
├── llm_backends/            
│   ├── serve_llama.py       # Launches and manages local Llama-3/DeepSeek/StarCoder LLM servers using vLLM or LMDeploy
│   ├── serve_coder.py       # Starts local code-centric LLMs for the Coder Agent
│   ├── client.py            # Provides unified API for all agents to make requests to local or cloud LLMs (e.g., GPT-4o, vLLM)
│   └── README.md            # Documents how to run/stop models, hardware requirements, troubleshooting
│
├── orchestrator/            
│   ├── scheduler.py         # Main brain: assigns tasks, controls agent sequence, handles resource scheduling (GPU/CPU handoff)
│   ├── task_queue.py        # Manages queue of pending/active tasks, experiment state, retries, and escalation for approval
│   ├── process_manager.py   # Controls all subprocesses (experiment runs, agent LLM servers), ensures clean resource release
│   └── __init__.py
│
├── experiment/              
│   ├── runner.py            # Runs code experiments as subprocesses or Docker containers; manages VRAM/CPU handoff; logs runtime info
│   ├── result_parser.py     # Parses experiment logs (stdout, stderr), extracts metrics, detects failures for Coder/Manager agents
│   ├── data_handler.py      # Loads, preprocesses, and splits datasets; verifies compatibility with agent-generated code
│   ├── env_manager.py       # Creates/destroys clean Python/conda/Docker environments for each experiment for full isolation
│   ├── job_templates/       # Boilerplate scripts that the Coder Agent can fill in (e.g., `pytorch_train_template.py`)
│   │   └── pytorch_train_template.py
│   └── __init__.py
│
├── memory/                  
│   ├── db.py                # Interface to SQLite or ChromaDB; stores agent memory, experiment metadata, code/idea history
│   ├── vector_store.py      # Optional: For retrieval-augmented memory (RAG); supports similarity search over logs/ideas/results
│   └── __init__.py
│
├── storage/                 
│   ├── experiments/         # All experiment folders—each run gets a unique folder (code, logs, results, models)
│   │   └── exp001/
│   │       ├── code/
│   │       ├── logs/
│   │       ├── models/
│   │       └── results/
│   └── .gitignore           # Ignore all experiment data and large files in git
│
├── configs/                 
│   ├── agents.yaml          # Settings for agent personalities, strictness, retry/approval logic, etc.
│   ├── llm_servers.yaml     # Config for local/cloud LLMs (model paths, endpoints, VRAM allocation, etc.)
│   ├── experiment.yaml      # Experiment parameters: benchmarks, dataset paths, result targets, resource limits
│   ├── datasets.yaml        # Info on supported datasets, schema, download scripts, etc.
│   └── workspace.yaml       # Paths and workspace options; e.g., location of storage, logs, DB
│
├── ui/                      
│   ├── web/                 
│   │   ├── app.py           # (Optional) Web dashboard for real-time monitoring, approvals, log review, and experiment control
│   │   └── ...
│   ├── cli/
│   │   └── main.py          # Command-line interface for all system controls, agent approvals, and monitoring
│   └── README.md
│
├── scripts/                 
│   ├── launch_agents.sh     # Bash script to start all agents and LLM servers in the correct order
│   ├── run_experiment.sh    # Launches a new experiment pipeline
│   ├── clean_gpu.sh         # Utility to kill stray processes and free VRAM
│   ├── backup_db.sh         # Script for periodic backup of all logs, memory, and experiment results
│   └── ...
│
├── tests/                   
│   ├── test_agents.py       # Unit tests for agent logic, prompt/response sanity, etc.
│   ├── test_runner.py       # Tests for experiment execution, resource isolation, and error handling
│   └── ...
│
├── requirements.txt         # All Python dependencies (for main pipeline, agents, and experiments)
├── Dockerfile               # (Optional) To run the system reproducibly anywhere
├── README.md                # Top-level project overview, install/setup instructions, usage guide
└── LICENSE



Folder/File Explanations
1. agents/

Handles all agent-specific logic:

    idea_agent.py: Connects to GPT-4o, generates, refines, and logs new research ideas.

    coder_agent.py: Receives ideas, writes code, handles code generation/fixes, and tracks past errors.

    manager_agent.py: Checks feasibility, enforces experiment policy, decides when to re-try, halt, or escalate for approval (including human-in-the-loop).

    reviewer_agent.py: Parses experiment results, makes plots, validates claims, and prepares publication-ready summaries.

2. llm_backends/

Everything for managing local and remote LLMs:

    serve_llama.py, serve_coder.py: Start/stop Llama, DeepSeek, or StarCoder servers on your hardware.

    client.py: Unified API to make LLM calls, whether local or cloud (GPT-4o via OpenAI API).

    README.md: How to set up, configure, and monitor your model servers.

3. orchestrator/

Controls overall flow and scheduling:

    scheduler.py: Controls sequence of agent calls, timing, and GPU/CPU handoff.

    task_queue.py: Queues tasks (experiments, codegen, approvals), tracks state.

    process_manager.py: Launches/kills subprocesses, ensures no VRAM/CPU/RAM leaks, and logs failures for diagnosis.

4. experiment/

Handles experiment runs and resource management:

    runner.py: Launches code (as a subprocess or Docker), monitors resource usage, cleans up after runs.

    result_parser.py: Extracts metrics from logs, detects NaNs or suspicious results.

    data_handler.py: Loads, splits, and validates input data for experiments.

    env_manager.py: Prepares fresh Python/conda/Docker environments for each experiment.

    job_templates/: Boilerplate code scripts the Coder Agent can fill in.

5. memory/

Persistent logs, experiment tracking, and agent memory:

    db.py: Handles connection to SQLite/Chroma for storing every idea, code version, and result.

    vector_store.py: Used for similarity search—retrieval-augmented memory, letting agents “remember” and “search” past attempts.

6. storage/

On-disk, permanent storage of all code, logs, models, and results for every experiment.
7. configs/

All system configs in editable YAML/JSON files.

    Tweak agent personalities, LLM settings, experiment policies, resource limits, and storage paths without code changes.

8. ui/

Optional dashboard/CLI for interacting with the system.

    Web: Real-time monitoring and control (start, stop, approve).

    CLI: Headless, scriptable access for power users.

9. scripts/

Convenience scripts to start, stop, backup, or clean up the system.
10. tests/

Unit and integration tests for every module—ensures system stability and reliability.
How This Structure Helps

    Separation of concerns: Each agent and function has its own module, easy to test and extend.

    Scalable & robust: Experiment outputs don’t clutter RAM, and all failures are logged and recoverable.

    Enterprise-ready: Clean configs, modular code, and test coverage make hand-off and onboarding smooth.

    Hybrid-ready: Supports local + cloud agents (GPT-4o for idea generation) with minimal friction.






+-------------------+      +---------------------+      +------------------+
|   Idea Agent      |----->|   Manager Agent     |----->|   Coder Agent    |
| (generates ideas) |      | (approves, plans)   |      | (codes, executes)|
+-------------------+      +---------------------+      +------------------+
           ^                            |                        |
           |                            v                        v
           |                      +------------------+    +---------------+
           |                      | Reviewer Agent   |<---| Experiment DB |
           |                      | (analyzes, logs) |    +---------------+
           +--------------------------------------------------+
