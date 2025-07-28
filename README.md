
# ✨ Kids Story Creation Pipeline

## 📘 Overview

This repository contains a modular pipeline for creating meaningful and engaging children's stories using three distinct agents using Azure Autogen AI and Azure OpenAi:

- **Story_writer**: Crafts and corrects the story.
- **Story_reviewer**: Evaluates the story for kid-friendliness and suggests improvements.
- **Story_moral**: Adds a positive moral to the final version of the story.
- **PlanningAgent**: An agent for planning tasks, this agent should be the first to engage when given a new task.

Each agent performs a specific role in the storytelling process, ensuring the final output is creative, appropriate, and impactful.

---

## 🧠 Agents

### 🖋️ Story_writer
- **Purpose**: Generates the initial story and performs corrections.
- **Responsibilities**:
  - Writes original stories.
  - Fixes grammar, structure, and flow.
  - Ensures the story is suitable for children.

### 🔍 Story_reviewer
- **Purpose**: Reviews the story for kid-friendliness and suggests improvements.
- **Responsibilities**:
  - Checks if the story is appropriate for children.
  - Provides constructive feedback.
  - Suggests enhancements to the ending for a positive impact.
  - **Note**: Does **not** write or rewrite the story.

### 🌟 Story_moral
- **Purpose**: Adds a moral to the final version of the story.
- **Responsibilities**:
  - Reads the revised story.
  - Appends a clear and relevant moral.
  - Ensures the moral aligns with the story’s theme.
 
    ### 🌟 PlanningAgent
- **Purpose**: An agent for planning tasks, this agent should be the first to engage when given a new task.
- **Responsibilities**:
  - Your job is to break down complex tasks into smaller, manageable subtasks.
  - Assigns tasks to agents rather than doing itself
  - After all tasks are complete, summarize the findings and end with "TERMINATE".

---
