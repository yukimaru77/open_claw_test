from __future__ import annotations

import argparse
from importlib.metadata import PackageNotFoundError, version

DEFAULT_NAME = "uv"


def get_version() -> str:
    try:
        return version("minimal-uv-project")
    except PackageNotFoundError:
        return "dev"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="open-claw-test",
        description="A small sample CLI for the open_claw_test repository.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {get_version()}",
    )

    subparsers = parser.add_subparsers(dest="command")

    greet_parser = subparsers.add_parser("greet", help="Print a greeting.")
    greet_parser.add_argument("name", nargs="?", default=DEFAULT_NAME, help="Name to greet.")
    greet_parser.add_argument("-t", "--times", type=int, default=1, help="How many times to print the greeting.")
    greet_parser.add_argument("--uppercase", action="store_true", help="Print the greeting in uppercase.")

    info_parser = subparsers.add_parser("info", help="Show project information.")
    info_parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format.")

    return parser


def run_greet(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    if args.times < 1:
        parser.error("--times must be 1 or greater")

    message = f"Hello, {args.name}!"
    if args.uppercase:
        message = message.upper()

    for _ in range(args.times):
        print(message)

    return 0


def run_info(args: argparse.Namespace) -> int:
    project_info = {
        "name": "minimal-uv-project",
        "cli": "open-claw-test",
        "version": get_version(),
        "python": ">=3.11",
    }

    if args.format == "json":
        import json

        print(json.dumps(project_info, ensure_ascii=False, indent=2))
    else:
        for key, value in project_info.items():
            print(f"{key}: {value}")

    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command in (None, "greet"):
        if args.command is None:
            args = parser.parse_args(["greet"])
        return run_greet(args, parser)

    if args.command == "info":
        return run_info(args)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
