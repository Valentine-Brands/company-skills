# Repository instructions

## Purpose

This public repository distributes shared Agent Skills for Claude Code and Codex.

## Sources of truth

- `plugins/company-skills/skills/` contains the maintained skill source.
- `plugins/company-skills/.claude-plugin/plugin.json` packages the skills for Claude Code.
- `plugins/company-skills/.codex-plugin/plugin.json` packages the same skills for Codex.
- `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` publish the plugin catalogs.

Do not maintain duplicate skill copies for different agents.

## Changes

- Treat every committed file as public. Do not include personal account names, local paths, internal hosts, credentials, or private operational details.
- Give each skill one clear responsibility and keep its description specific enough for reliable discovery.
- Put repeated deterministic operations in `scripts/`. Put conditional background material in `references/`.
- Keep the Claude and Codex plugin versions aligned. Bump both versions for a plugin release.
- Validate changed skills and both plugin manifests before release.
- Do not create, delete, publish, or deploy external resources without explicit user authorization.
