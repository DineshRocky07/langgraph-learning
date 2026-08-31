flowchart TB
    %% STYLING
    classDef title fill:#000,stroke:#fff,color:#fff,font-size:20px,font-weight:bold,stroke-width:2px;
    classDef section fill:#333,stroke:#666,color:#fff,font-size:16px,font-weight:bold;
    classDef archNode fill:#1565C0,stroke:#0D47A1,color:#fff,stroke-width:2px;
    classDef actionNode fill:#E65100,stroke:#BF360C,color:#fff,stroke-width:2px;
    classDef routerNode fill:#4A148C,stroke:#311B92,color:#fff,stroke-width:2px;
    classDef textNode fill:#f8f9fa,stroke:#adb5bd,color:#212529,text-align:left;
    classDef memNode fill:#e9ecef,stroke:#6c757d,color:#212529,text-align:left,stroke-width:2px;

    %% MAIN TITLE
    TITLE(["🦜🕸️ LANGGRAPH REACT ARCHITECTURE: THE CONCEPTUAL GUIDE"]):::title

    %% ==========================================
    %% SECTION 1: ARCHITECTURE & COMPONENTS
    %% ==========================================
    subgraph S1 ["1. HIGH-LEVEL ARCHITECTURE & COMPONENT BREAKDOWN"]
        direction LR
        START([🚪 START]) --> REASON["🧠 Reasoning Engine (LLM)<br/><i>Analyzes history -> Tool Request OR Final Answer</i>"]:::archNode
        REASON --> ROUTER{"🔀 Router<br/><i>Did AI ask for a tool?</i>"}:::routerNode
        ROUTER -- "YES 🛠️" --> ACTION["⚙️ Action Engine<br/><i>Executes external tools -> Raw Data</i>"]:::actionNode
        ROUTER -- "NO 🏁" --> END([🛑 END])
        ACTION -->|"Updates Memory & Loops Back"| REASON
    end

    %% ==========================================
    %% SECTION 2: THE 4 PILLARS & WORKERS (TABLES)
    %% ==========================================
    subgraph S2 ["2. THE 4 PILLARS & WORKER IDENTITIES"]
        direction TB
        
        PILLARS["`**THE 4 PILLARS OF LANGGRAPH**
        **1. State (Memory):** A shared, append-only ledger (Team Whiteboard). Keeps track of User queries, AI thoughts, and Tool outputs.
        **2. Nodes (Workers):** The processing units (Employees). Reads State, does work, writes new data.
        **3. Edges (Paths):** Fixed connections (Hallways). Ensures the Action Engine always sends results back to the Reasoner.
        **4. Conditional Edges:** Dynamic routers (Security Guard). Decides if task is finished or more tools needed.`"]:::textNode

        WORKERS["`**COMPONENT IDENTITIES**
        🧠 **Reasoning Engine (AI / LLM):** 
        *Role:* Analyzes history & decides next logical step. 
        *Output:* Tool Request OR Final Answer.
        
        ⚙️ **Action Engine (Tool Executor):** 
        *Role:* Blindly executes tools the AI requested. 
        *Output:* Raw Data / Results from external tools.`"]:::textNode
        
        PILLARS --- WORKERS
    end

    %% ==========================================
    %% SECTION 3: EXECUTION TRACE & MEMORY LIFECYCLE
    %% ==========================================
    subgraph S3 ["3. MULTI-STEP EXECUTION TRACE & MEMORY LIFECYCLE (Prompt: 'Find weather in SF and triple it')"]
        direction TB

        STEP1["`**STEP 1: Start (User Input)**
        *Who:* User
        *Action:* Adds query to memory
        *State Contains:* **[User Query]**`"]:::memNode

        STEP2["`**STEP 2: Loop 1 - Information Gathering (Reasoning)**
        *Who:* 🧠 Reasoning Engine
        *Action:* Reads history, asks for Search Tool
        *State Contains:* **[User Query, AI Tool Req 1]**`"]:::memNode

        STEP3["`**STEP 3: Loop 1 - Information Gathering (Action)**
        *Who:* ⚙️ Action Engine & 🔀 Router
        *Action:* Router sees tool req -> Action Engine searches -> '60 Degrees'
        *State Contains:* **[User Query, AI Req 1, Tool Result 1]**`"]:::memNode

        STEP4["`**STEP 4: Loop 2 - Calculation (Reasoning)**
        *Who:* 🧠 Reasoning Engine
        *Action:* Reads Query + Search Result, asks for Math Tool
        *State Contains:* **[..., Tool Res 1, AI Tool Req 2]**`"]:::memNode

        STEP5["`**STEP 5: Loop 2 - Calculation (Action)**
        *Who:* ⚙️ Action Engine & 🔀 Router
        *Action:* Router sees tool req -> Action Engine does Math -> '180'
        *State Contains:* **[..., AI Req 2, Tool Result 2]**`"]:::memNode

        STEP6["`**STEP 6: Loop 3 - Final Synthesis**
        *Who:* 🧠 Reasoning Engine
        *Action:* Reads full history, pieces it together, outputs conversational answer
        *State Contains:* **[..., Tool Res 2, AI Final Answer]**`"]:::memNode

        STEP7["`**STEP 7: Task Complete**
        *Who:* 🔀 Router
        *Action:* Inspects absolute latest message, sees NO tool calls -> Routes to END
        *Result:* User receives final response`"]:::memNode

        STEP1 --> STEP2 --> STEP3 --> STEP4 --> STEP5 --> STEP6 --> STEP7
    end

    %% CONNECT SECTIONS
    TITLE ~~~ S1
    S1 ~~~ S2
    S2 ~~~ S3