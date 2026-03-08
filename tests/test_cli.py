from __future__ import annotations

import contextlib
import io
import json
import unittest
from unittest.mock import patch

import minimal_uv_project
import open_claw_test_cli


class MinimalUvProjectTests(unittest.TestCase):
    def run_main(self, argv: list[str]) -> str:
        buf = io.StringIO()
        with patch("sys.argv", ["minimal-uv-project", *argv]):
            with contextlib.redirect_stdout(buf):
                minimal_uv_project.main()
        return buf.getvalue()

    def test_minimal_cli_repeats_greeting(self) -> None:
        output = self.run_main(["Alice", "--times", "2"])
        self.assertEqual(output, "Hello, Alice!\nHello, Alice!\n")

    def test_minimal_cli_uppercase(self) -> None:
        output = self.run_main(["Bob", "--uppercase"])
        self.assertEqual(output, "HELLO, BOB!\n")


class OpenClawTestCliTests(unittest.TestCase):
    def run_main(self, argv: list[str]) -> tuple[int, str]:
        buf = io.StringIO()
        with patch("sys.argv", ["open-claw-test", *argv]):
            with contextlib.redirect_stdout(buf):
                exit_code = open_claw_test_cli.main()
        return exit_code, buf.getvalue()

    def test_default_invocation_runs_greet_with_default_name(self) -> None:
        exit_code, output = self.run_main([])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output, "Hello, uv!\n")

    def test_greet_uppercase_and_repeat(self) -> None:
        exit_code, output = self.run_main(["greet", "Carol", "--times", "2", "--uppercase"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output, "HELLO, CAROL!\nHELLO, CAROL!\n")

    def test_info_json_output(self) -> None:
        exit_code, output = self.run_main(["info", "--format", "json"])
        self.assertEqual(exit_code, 0)
        data = json.loads(output)
        self.assertEqual(data["name"], "minimal-uv-project")
        self.assertEqual(data["cli"], "open-claw-test")
        self.assertEqual(data["python"], ">=3.11")
        self.assertIn("version", data)


if __name__ == "__main__":
    unittest.main()
