---
name: create-company-app
description: Create a new application from the Valentine Brands public starter repository. Use when someone asks to start, scaffold, or set up a company app. Do not use for changing an existing application.
---

# Create Company App

Create the project from `https://github.com/Valentine-Brands/company-app-template` and then adapt it to the requested application.

## Workflow

1. Establish the application name, business purpose, destination directory, and required user-facing behavior. Ask only for choices that materially change the result.
2. Check the destination before writing. Do not overwrite a non-empty directory.
3. Run `scripts/create_project.py <destination> --name <project-name>`, resolving the script relative to this `SKILL.md` file. The script copies the starter and initializes a fresh local Git repository.
4. Inspect the generated `AGENTS.md` and the starter files before choosing a technical stack.
5. Build the smallest application that satisfies the stated behavior. Keep stack decisions visible in the generated README.
6. Run the checks documented by the resulting project and report anything that still needs a user decision.

## Boundaries

- Do not create a remote repository, push code, deploy, purchase services, or configure production resources unless the user explicitly requests that action.
- Never copy credentials or populated environment files into the project. Use `.env.example` for required variable names.
- Preserve existing files when the user intentionally targets an existing empty or prepared directory.
