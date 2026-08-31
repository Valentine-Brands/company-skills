---
name: change-company-database
description: Plan, implement, and verify schema and access-control changes for company applications using Supabase Postgres. Use when adding or changing tables, columns, constraints, indexes, RLS policies, views, functions, triggers, migrations, or application-owned seed data. Do not use for routine read-only data questions.
---

# Change Company Database

Keep every database change reproducible in Git and safe for a company application that normally uses one hosted Supabase project.

## Sources of truth

1. Read `AGENTS.md`, `README.md`, `supabase/config.toml`, and existing files in `supabase/migrations` when they exist.
2. Use the current official Supabase documentation as the technical source of truth.
3. Use the official `supabase` and `supabase-postgres-best-practices` skills when they are installed. Do not install them or other tools without the user's permission.
4. Inspect the installed Supabase CLI with `supabase --help` before relying on a command or option. If it is not installed, ask before downloading it through `npx supabase`.

## Database model

Assume the application has one hosted Supabase project. Do not require Docker, a local database, Supabase Branching, or a separate development project.

Before changing the database, determine whether it contains real user, customer, or business data. If this cannot be confirmed, treat the database as production.

Repository access does not authorize remote database access. Identify the exact Supabase project and whether the requested operation is read-only or mutating before using any remote tool.

## Inspect the database

Use project-scoped, read-only Supabase access when it is available and authorized. Inspect only the schema, migration history, policies, advisors, and small query results needed for the task.

Do not retrieve whole tables, authentication records, customer data, or unrelated business data. Never display connection strings, access tokens, database passwords, secret keys, or personal data.

When the project contains real data, keep Supabase MCP read-only. Do not enable write access for MCP against that project.

## Prepare a migration

Track every schema change in `supabase/migrations`.

1. Compare the existing migration files with the remote migration history when authorized access is available.
2. Create a migration with `supabase migration new <descriptive-name>`. This creates a file and does not require a running local database. Use `npx supabase` only when the user has approved that fallback.
3. Add the SQL for one logical change.
4. Review the SQL for data loss, locks, RLS, and compatibility with the running application.
5. Commit the migration in the current feature branch and merge it through the repository's Pull Request workflow.

Never edit a migration that has already been applied or shared. Create a new migration instead.

Do not leave a schema change only in the Table Editor, SQL Editor, or MCP `execute_sql`. The final change must exist as a migration in Git. If an experiment changed the remote schema, capture and reconcile it before completing the task.

## Protect existing data

Prefer additive changes. Add the new structure, update the application, backfill when needed, switch reads and writes, and remove the old structure in a later migration.

Do not automatically run operations that drop or truncate data, narrow a type, rewrite a large table, or update or delete rows without a restrictive condition. These operations require technical review, explicit authorization, and a confirmed recovery method.

## Secure Supabase access

- Enable RLS on every application table in a schema exposed through the Data API.
- Write policies for the actual ownership or organization model. `TO authenticated` alone is not authorization.
- Define both `USING` and `WITH CHECK` for update policies when ownership must remain unchanged.
- Do not use user-editable metadata for authorization.
- Keep `service_role`, secret keys, and database credentials on the server. Never place them in `NEXT_PUBLIC_*` variables.
- Prefer `security_invoker` views. Do not use `SECURITY DEFINER` to bypass a permission error.
- Keep privileged functions and internal tables in an unexposed schema when possible.

## Apply a migration

Preparing a migration does not authorize applying it remotely.

Before a remote change, state the exact project, migration filename, expected effect, and whether existing data may change. Obtain explicit authorization for that project and migration.

When the Supabase CLI is linked to the authorized project:

1. Run `supabase db push --dry-run` and review the pending migrations.
2. Apply them with `supabase db push` only after the review matches the approved change.
3. Allow only one migration deployment at a time.

If the project is confirmed to contain only test data, an authorized migration-capable Supabase tool may apply the exact SQL stored in Git. Do not use arbitrary write SQL when a versioned migration can represent the change.

Do not run seed data against a project with real data unless the user explicitly requests it and the seed is safe to run there.

## Verify the result

After applying a migration:

1. Confirm that it appears in the remote migration history.
2. Inspect the resulting tables, constraints, indexes, and RLS policies.
3. Run Supabase security and performance advisors when available.
4. Test the intended allowed and denied access paths without exposing real records.
5. Regenerate TypeScript database types using the project's documented location.
6. Run the application's typecheck and relevant tests.
7. Report what passed, failed, and was not tested.

If no database access is available, prepare the migration and report it as unapplied and unverified. If a migration fails, stop and diagnose the error. Do not retry modified SQL directly against the database or run `migration repair` without technical review.
