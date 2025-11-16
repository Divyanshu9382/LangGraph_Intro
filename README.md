# 🕸️ LangGraph Introduction

This project demonstrates the basics of LangGraph, a framework for building stateful, multi-actor applications with LLMs. 🤖✨

## 🤔 What is LangGraph?

LangGraph is a library for building stateful, multi-actor applications with LLMs, built on top of (and intended to be used with) LangChain. It extends the LangChain Expression Language with the ability to coordinate multiple chains (or actors) across multiple steps of computation in a cyclic manner. 🔄

## ⭐ Key Features

- 💾 **Stateful**: Maintains state across multiple interactions
- 👥 **Multi-actor**: Supports multiple agents working together
- 🔄 **Cyclic workflows**: Allows loops and conditional branching
- 💿 **Built-in persistence**: Can save and restore conversation state
- 🤝 **Human-in-the-loop**: Supports human intervention in workflows

## 🆚 LangGraph vs LangChain

| Feature | 🔗 LangChain | 🕸️ LangGraph |
|---------|-----------|-----------|
| **Workflow Type** | Linear chains | Cyclic graphs with loops |
| **State Management** | Stateless | Stateful with persistence |
| **Control Flow** | Sequential | Conditional branching & loops |
| **Multi-agent** | Limited | Native support |
| **Complexity** | Simple chains | Complex workflows |
| **Use Cases** | Basic Q&A, simple workflows | Agent systems, complex reasoning |

## 🚀 Why Use LangGraph?

1. 🧠 **Complex Reasoning**: Build ReAct agents that can reason and act iteratively
2. 🔄 **Multi-step Workflows**: Handle workflows that require multiple LLM calls
3. 💾 **State Persistence**: Maintain conversation context across interactions
4. 🌿 **Conditional Logic**: Implement branching logic based on LLM responses
5. 🛠️ **Tool Integration**: Seamlessly integrate external tools and APIs

## 📁 Project Structure

- 📄 `main.py` - Main application with ReAct agent workflow
- 🔧 `nodes.py` - Agent reasoning and tool execution nodes
- ⚛️ `react.py` - LLM configuration and tool definitions
- 🖼️ `flow.png` - Visual representation of the workflow graph

## ⚙️ Setup

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Set up environment variables in `.env`:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
   TAVILY_API_KEY=your_tavily_api_key
   ```

3. Run the application:
   ```bash
   poetry run python main.py
   ```

## 🔄 How It Works

This project implements a ReAct (Reasoning + Acting) pattern:

1. 🧠 **Agent Reasoning**: LLM analyzes the question and decides what tools to use
2. 🛠️ **Tool Execution**: Executes the selected tools (search, calculations)
3. 🌿 **Conditional Flow**: Continues until no more tools are needed
4. ✅ **Final Response**: Returns the complete answer

The workflow creates a cycle between reasoning and acting, allowing the agent to iteratively solve complex problems. 🔄💡