---
name: verify-company-app
description: Verify an existing company application before it is called complete or ready to release. Use for validation, readiness checks, or evidence-backed completion reports. Do not use to create an app or fix findings unless the user asks.
---

# Verify Company App

Verify the application that exists. Do not assume the planned stack or documented behavior matches the current code.

## Workflow

1. Read `AGENTS.md`, `README.md`, `package.json`, the lockfile, and the current Git status.
2. Use the package manager selected by the repository. Do not replace it or add verification dependencies.
3. Run the repository's documented verification command when it has one. Otherwise run the available lint, typecheck, test, and build scripts. Do not invent missing scripts.
4. Inspect the current changes for committed secrets, populated environment files, accidental local paths, and undocumented environment variable names.
5. When the change affects user behavior and the app can run locally, exercise the relevant workflow. Use browser verification only when it adds evidence that command-line checks cannot provide.
6. Report each check as passed, failed, or not run. Include the command or observation behind the result and state what remains untested.

## Boundaries

- Verification is read-only apart from temporary build and test output created by the project's own commands.
- Do not fix failures, update dependencies, change configuration, deploy, or modify external systems unless the user explicitly requests it.
- Do not describe an application as verified when only a subset of its checks ran.
