# 🔁 LangGraph Reflection Agent

An agentic workflow built with **LangGraph**, **LangChain**, and **Google Gemini 2.5 Flash** that implements the **Reflection Pattern** — where an AI generator drafts content, an influencer critic agent provides targeted feedback, and the generator iteratively refines the post until it reaches peak virality.

---

## 📌 Architecture & Workflow

The **Reflection Pattern** mimics the human drafting and review loop:

```mermaid
flowchart TD
    %% Entry Point
    __start__([Start: User Tweet Request]) --> generate[Generate Node<br/><i>Drafts Tweet via Gemini 2.5 Flash</i>]

    %% Conditional Check
    generate --> condition{History Length > 5?}

    %% Decision Branches
    condition -- "No (Needs Refinement)" --> reflect[Reflect Node<br/><i>Viral Influencer Critique</i>]
    reflect -->|Appends Critique to History| generate

    condition -- "Yes (Max Iterations Reached)" --> __end__([End: Final Polished Tweet])

    %% Styling
    classDef startEnd fill:#10b981,stroke:#059669,stroke-width:2px,color:#ffffff;
    classDef nodeStyle fill:#3b82f6,stroke:#1d4ed8,stroke-width:2px,color:#ffffff;
    classDef condStyle fill:#f59e0b,stroke:#d97706,stroke-width:2px,color:#ffffff;

    class __start__,__end__ startEnd;
    class generate,reflect nodeStyle;
    class condition condStyle;
```

![Graph Visualization](graph.png)

### The Iteration Cycle
1. **Generator Node (`generate`)**: An AI acting as a tech influencer writes an initial tweet based on the user's prompt.
2. **Conditional Edge (`should_continue`)**: Checks if the message history exceeds the iteration limit (`len(history) > 5`). If yes, the process completes (`END`).
3. **Reflector Node (`reflect`)**: A viral Twitter influencer agent critiques the draft on hooks, length, engagement, hashtags, and virality.
4. **Iterative Refinement**: The critique is appended back into the message history (`HumanMessage`), prompting the Generator to revise and improve in the next cycle.

---

## 🛠️ Project Structure

```text
langgraph_reflection_agent/
├── chains.py          # Generator & Reflection prompt templates + Gemini LLM chains
├── main.py            # LangGraph StateGraph, nodes, conditional edges & execution
├── graph.png          # Visual export of the compiled LangGraph workflow
├── pyproject.toml     # Poetry dependencies & project metadata
└── README.md          # Project documentation
```

---

## 🧠 Core Components Explained

### 1. `chains.py` — Prompt Engineering & LCEL
- **`ChatPromptTemplate.from_messages`**: Structures the conversation history with clear system instructions and contextual dialog.
- **`MessagesPlaceholder(variable_name="history")`**: Injects dynamic message history into the prompt at runtime so both agents remember prior drafts and critiques.
- **`ChatGoogleGenerativeAI`**: Leverages `gemini-2.5-flash` for high-speed, cost-effective inference.
- **LangChain Expression Language (LCEL)**:
  ```python
  generation_chain = generation_prompt | llm
  reflection_chain = reflection_prompt | llm
  ```

### 2. `main.py` — Graph State & Control Flow
- **`TypedDict` & `Annotated`**: Defines typed graph state.
- **`add_messages` Reducer**: Tells LangGraph to **append** new messages to `history` instead of overwriting the previous state.
  ```python
  class Messagegraph(TypedDict):
      history: Annotated[list[BaseMessage], add_messages]
  ```
- **Conditional Routing**:
  ```python
  def should_conitue(state: Messagegraph):
      if len(state["history"]) > 5:
          return END
      return REFLECT

  builder.add_conditional_edges(
      GENERATE,
      should_conitue,
      {
          REFLECT: REFLECT,
          END: END
      }
  )
  ```

---

## 🚀 Getting Started

### Prerequisites
- Python **3.12+**
- [Poetry](https://python-poetry.org/) package manager
- Google Gemini API Key ([Get one from Google AI Studio](https://aistudio.google.com/))

### 1. Installation
Clone the repository and install dependencies with Poetry:

```bash
git clone https://github.com/DineshRocky07/langgraph-learning.git
cd langgraph-learning/langgraph_reflection_agent
poetry install
```

### 2. Environment Setup
Create a `.env` file in the project root:

```env
GOOGLE_API_KEY="your-google-gemini-api-key"
```

### 3. Run the Agent

```bash
poetry run python main.py
```

---

## 💡 Quick Reference: Agentic AI Concepts

| Term | Definition | Role in this Project |
|---|---|---|
| **LLM** | The foundational reasoning brain | `gemini-2.5-flash` powering generation & critique |
| **Prompt** | System instructions and persona definition | Viral tech writer persona & strict critique rubric |
| **Chain** | Connected Prompt + Model pipeline | `generation_prompt \| llm` |
| **StateGraph** | Orchestrator of cyclic, stateful workflows | Controls `generate ⇄ reflect` iteration loops |
| **Reducer (`add_messages`)** | State accumulator function | Automatically appends iterations without losing chat history |
| **Reflection** | Self-correction / feedback loop | Iteratively transforms average output into high-performing content |

---

## 📜 License

This project is licensed under the MIT License. Created as part of the LangGraph Learning series by [@DineshRocky07](https://github.com/DineshRocky07).
