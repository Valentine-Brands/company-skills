#!/usr/bin/env python3
"""Copy the public company app starter into a new local Git repository."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path


DEFAULT_TEMPLATE = "https://github.com/Valentine-Brands/company-app-template.git"


def run(*args: str, cwd: Path | None = None) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an application from the company starter repository."
    )
    parser.add_argument("destination", type=Path)
    parser.add_argument("--name", required=True, help="Human-readable application name")
    parser.add_argument("--template", default=DEFAULT_TEMPLATE)
    parser.add_argument(
        "--no-git",
        action="store_true",
        help="Do not initialize a fresh local Git repository",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    name = args.name.strip()
    if not name or "\n" in name or "\r" in name:
        raise SystemExit("--name must be a non-empty single line")

    destination = args.destination.expanduser().resolve()
    if destination.exists() and any(destination.iterdir()):
        raise SystemExit(f"Destination is not empty: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="company-app-template-") as temp_dir:
        checkout = Path(temp_dir) / "starter"
        run("git", "clone", "--depth", "1", args.template, str(checkout))
        shutil.rmtree(checkout / ".git")
        shutil.copytree(checkout, destination, dirs_exist_ok=destination.exists())

    readme = destination / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8")
        content = content.replace("# Company App Template", f"# {name}", 1)
        readme.write_text(content, encoding="utf-8")

    if not args.no_git:
        run("git", "init", "-b", "main", cwd=destination)

    print(destination)


if __name__ == "__main__":
    main()
