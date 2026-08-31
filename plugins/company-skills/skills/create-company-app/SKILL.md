---
name: create-company-app
description: Create a new application from the Valentine Brands public starter repository. Use when someone asks to start, scaffold, or set up a company app. Do not use for changing an existing application.
---

# Create Company App

Create the project from `https://github.com/Valentine-Brands/company-app-template` and then adapt it to the requested application.

## Workflow

1. Establish the application name, business purpose, destination directory, intended users, and required user-facing behavior. Ask only for choices that materially change the result.
2. Clarify whether users must sign in, whether the app connects to outside services, and whether anything must happen automatically at a specific time, such as a daily data import or report.
3. Check the destination before writing. Do not overwrite a non-empty directory.
4. Run `scripts/create_project.py <destination> --name <project-name>`, resolving the script relative to this `SKILL.md` file. The script copies the starter and initializes a fresh local Git repository.
5. Read the generated `AGENTS.md` before selecting dependencies or services. Use its default stack unless a concrete requirement justifies another choice, and document any exception in the generated README.
6. Build the smallest application that satisfies the stated behavior. Add Supabase, authentication, outside integrations, or automatic time-based tasks only when the requirements need them.
7. Update the README and `.env.example`, run the checks documented by the resulting project, and report anything that still needs a user decision.

## Boundaries

- Do not create a remote repository, push code, deploy, purchase services, or configure production resources unless the user explicitly requests that action.
- Never copy credentials or populated environment files into the project. Use `.env.example` for required variable names.
- Preserve existing files when the user intentionally targets an existing empty or prepared directory.
