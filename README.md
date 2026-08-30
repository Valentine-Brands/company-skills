# Company Skills

Public Agent Skills maintained by Valentine Brands for Claude Code and Codex.

## Available skills

### `create-company-app`

Creates a new local application from the public [`company-app-template`](https://github.com/Valentine-Brands/company-app-template) repository and guides the agent through adapting it to the requested product.

## Install in Claude Code

```text
/plugin marketplace add Valentine-Brands/company-skills
/plugin install company-skills@valentine-brands
```

## Install in Codex

Add the Git-backed marketplace:

```bash
codex plugin marketplace add Valentine-Brands/company-skills
```

Then open the Plugins Directory and install `company-skills` from the Valentine Brands marketplace.

## Updating

Claude Code users can refresh the marketplace and plugin from `/plugin`. Codex users can refresh the marketplace with:

```bash
codex plugin marketplace upgrade valentine-brands
```

The plugin contains no credentials or private company configuration.
