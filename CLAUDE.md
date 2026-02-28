# Claude Configuration

## General Preferences
- Keep responses concise and to the point
- Always explain what you're doing before making changes
- Ask before making destructive changes (delete, overwrite, force push)

## Code Style
- Follow existing project conventions
- Prefer readable code over clever code
- Add comments only when logic isn't self-evident

## Git & Version Control - STRICT REQUIREMENTS
- **ALWAYS create a feature branch** - Never work directly on main/master/develop
- **Branch naming convention**: Use descriptive names like `feature/add-authentication`, `fix/login-bug`, `refactor/api-cleanup`
- **Never push directly to main/master** - Always use pull requests for code review
- Create clear, descriptive commit messages following conventional commits (feat:, fix:, docs:, refactor:, test:, chore:)
- Never force push to main/master
- Always run tests before committing
- Keep commits atomic and focused on a single change
- Rebase feature branches on main before creating PR to keep history clean

## DevOps Best Practices - MANDATORY
- **Branch Strategy**: Always work on feature branches, never directly on main/master/develop
  - Create branch: `git checkout -b feature/description`
  - Keep branches short-lived (merge within days, not weeks)
  - Delete branches after merging
- **Pull Request Workflow**:
  - Push feature branch and create PR for review
  - Never merge your own PRs without approval (unless explicitly told)
  - Include clear PR descriptions with context and testing notes
- **CI/CD Compliance**:
  - Ensure all CI checks pass before requesting review
  - Fix linting, tests, and security scans
  - Never bypass CI checks unless explicitly authorized
- **Code Review**:
  - Make changes reviewable (small, focused PRs)
  - Respond to review comments before merging
- **Testing**:
  - Write tests for new features
  - Ensure existing tests pass
  - Don't skip test runs to "save time"
- **Documentation**:
  - Update README when adding features
  - Document configuration changes
  - Keep API docs in sync with code
- **Security**:
  - Never commit secrets, API keys, or credentials
  - Use environment variables for sensitive data
  - Scan for security vulnerabilities before PR

## Communication
- Show me what you're going to do before doing it
- If unsure, ask questions
- Provide context when suggesting changes

## Don't - CRITICAL PROHIBITIONS
- **NEVER push directly to main/master/develop** - Always use feature branches and PRs
- **NEVER force push to main/master** - This can destroy team work
- **NEVER commit secrets or credentials** - Use environment variables
- **NEVER skip tests** - They exist for a reason
- **NEVER bypass CI/CD checks** - Without explicit authorization
- Don't create unnecessary files
- Don't add features I didn't ask for
- Don't skip error handling for edge cases
- Don't merge without code review (unless explicitly told to)
- Don't make breaking changes without discussion
