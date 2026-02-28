# Recommended Claude Code Plugins

This document lists the recommended plugins for an optimal Claude Code experience, aligned with DevOps best practices.

## Enabled Plugins

### Code Quality & Review
- **code-simplifier** - Reviews code for reuse opportunities, quality issues, and efficiency
- **code-review** - Automated code review capabilities
- **pr-review-toolkit** - Comprehensive PR review with specialized agents:
  - `code-reviewer` - Full code reviews
  - `code-simplifier` - Code simplification
  - `comment-analyzer` - PR comment analysis
  - `pr-test-analyzer` - Test coverage analysis
  - `silent-failure-hunter` - Hidden bug detection
  - `type-design-analyzer` - Type system analysis
- **coderabbit** - CodeRabbit AI-powered code reviews

### Git & Version Control
- **commit-commands** - Enhanced commit workflows with conventional commits
  - Skills: `commit`, `commit-push-pr`, `clean_gone`

### Development Workflow
- **feature-dev** - Guided feature development with architecture focus
  - Agents: `code-architect`, `code-explorer`, `code-reviewer`
- **superpowers** - Advanced development workflows
  - Skills: TDD, systematic debugging, brainstorming, git worktrees, parallel agents, plan execution

### Frontend Development
- **frontend-design** - Production-grade frontend interface creation
  - Creates distinctive, polished UI components

### Security
- **security-guidance** - Security best practices and vulnerability detection

### Utilities
- **playground** - Creates interactive HTML playgrounds and explorers
- **skill-creator** - Create and optimize custom skills

## Installation

Add these to your `~/.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "code-simplifier@claude-plugins-official": true,
    "code-review@claude-plugins-official": true,
    "commit-commands@claude-plugins-official": true,
    "pr-review-toolkit@claude-plugins-official": true,
    "security-guidance@claude-plugins-official": true,
    "feature-dev@claude-plugins-official": true,
    "frontend-design@claude-plugins-official": true,
    "superpowers@claude-plugins-official": true,
    "playground@claude-plugins-official": true,
    "skill-creator@claude-plugins-official": true,
    "coderabbit@claude-plugins-official": true
  }
}
```

Or install via CLI:
```bash
/plugins
```

## Key Skills Available

After installing these plugins, you'll have access to these skills (use `/skills` to see all):

### Development Workflow
- `brainstorming` - Explore requirements before implementation
- `test-driven-development` - TDD workflow
- `systematic-debugging` - Structured bug fixing
- `feature-dev` - Guided feature development

### Code Quality
- `simplify` - Code simplification and refactoring
- `code-review` - Code review
- `review-pr` - Comprehensive PR review
- `requesting-code-review` - Request code review
- `receiving-code-review` - Handle code review feedback

### Git Operations
- `commit` - Create commits
- `commit-push-pr` - Commit, push, and create PR
- `clean_gone` - Clean up deleted branches
- `using-git-worktrees` - Work in isolated worktrees
- `finishing-a-development-branch` - Complete and integrate work

### Planning & Execution
- `writing-plans` - Create implementation plans
- `executing-plans` - Execute plans with review checkpoints
- `verification-before-completion` - Verify work before claiming completion

### Parallel Work
- `dispatching-parallel-agents` - Run independent tasks in parallel
- `subagent-driven-development` - Execute plans with independent tasks

### Content Creation
- `frontend-design` - Create frontend interfaces
- `playground` - Create interactive HTML tools
- `skill-creator` - Create custom skills

## Usage Tips

1. **Use skills proactively** - If there's even a 1% chance a skill applies, use it
2. **Follow DevOps practices** - Always create feature branches, never push to main
3. **Leverage specialized agents** - Use agents from pr-review-toolkit and feature-dev
4. **Enable security scanning** - security-guidance helps prevent vulnerabilities
5. **Use TDD workflow** - test-driven-development ensures quality

## Plugin Management

**View installed plugins:**
```bash
/plugins
```

**View available skills:**
```bash
/skills
```

**View available agents:**
```bash
/agents
```

## Syncing Across Machines

After cloning this repository:

1. Copy the plugin configuration to your settings:
   ```bash
   # Add the enabledPlugins section from this file to ~/.claude/settings.json
   ```

2. Restart Claude Code to load plugins

3. Verify plugins are loaded:
   ```bash
   /skills
   ```
