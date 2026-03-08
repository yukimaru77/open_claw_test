from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="minimal-uv-project",
        description="A tiny example CLI built with Python and uv.",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="uv",
        help="Name to greet.",
    )
    parser.add_argument(
        "-t",
        "--times",
        type=int,
        default=1,
        help="How many times to print the greeting.",
    )
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="Print the greeting in uppercase.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.times < 1:
        parser.error("--times must be 1 or greater")

    message = f"Hello, {args.name}!"
    if args.uppercase:
        message = message.upper()

    for _ in range(args.times):
        print(message)


if __name__ == "__main__":
    main()
