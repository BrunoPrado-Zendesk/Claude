# Custom Claude Code Agents

This directory contains custom agent definitions for Claude Code.

## What are Agents?

Agents are specialized AI assistants with specific expertise, tools, and system prompts. They can be invoked in Claude Code to handle domain-specific tasks.

## Available Agents

### zendesk-ai-sales-specialist

**Purpose:** Expert guidance on Zendesk's AI products (AI Agents, Copilot, QA, Full Resolution Platform), sales positioning, competitive analysis, and customer engagement strategies.

**Use cases:**
- Preparing for customer meetings about AI automation
- Competitive positioning against other platforms
- Demo structure and strategy
- Sales enablement and product positioning

**How to use:**
1. Copy the agent file to your local agents directory:
   ```bash
   cp agents/zendesk-ai-sales-specialist.md ~/.claude/agents/
   ```

2. Invoke in Claude Code by asking questions like:
   - "I have a call with a retail customer tomorrow who wants to reduce support tickets. What should I focus on?"
   - "A prospect is comparing us to Intercom's AI features. How do we differentiate?"
   - "Can you help me structure a demo for a financial services company interested in AI Agents?"

## Creating Your Own Agents

Agents are defined in Markdown files with YAML frontmatter. See the existing agents for examples.

**Basic structure:**
```markdown
---
name: my-agent-name
description: "What this agent does..."
model: opus  # or sonnet, haiku
color: cyan  # terminal display color
memory: project  # or global
---

Your agent's system prompt goes here...
```

## Installing Agents

To use these agents on a new machine:

```bash
# Clone this repository
git clone https://github.com/BrunoPrado-Zendesk/Claude.git

# Copy agents to Claude Code agents directory
cp Claude/agents/*.md ~/.claude/agents/
```
