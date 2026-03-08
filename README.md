# minimal-uv-project

`uv` を使った最小構成の Python プロジェクトです。

このリポジトリには 2 つの CLI があります。

- `minimal-uv-project`: 最小の greet CLI
- `open-claw-test`: サブコマンド付きのサンプル CLI

## 必要環境

- `uv`
- Python 3.11 以上

## セットアップ

```bash
uv sync
```

## 実行方法

### 既存の最小 CLI

```bash
uv run python minimal_uv_project.py Alice --times 2
uv run minimal-uv-project Bob --uppercase
```

### 追加した CLI

```bash
uv run open-claw-test greet Alice --times 2
uv run open-claw-test greet Bob --uppercase
uv run open-claw-test info
uv run open-claw-test info --format json
```

### ヘルプ表示

```bash
uv run open-claw-test --help
uv run open-claw-test greet --help
```

## `open-claw-test` CLI仕様

### `greet` サブコマンド

- `name`: あいさつする相手の名前（省略時は `uv`）
- `-t`, `--times`: あいさつを表示する回数
- `--uppercase`: あいさつを大文字で表示

### `info` サブコマンド

- プロジェクト名、CLI 名、バージョン、Python 要件を表示
- `--format json` で JSON 出力

## プロジェクト構成

```text
.
├── .gitignore
├── .python-version
├── README.md
├── minimal_uv_project.py
├── open_claw_test_cli.py
└── pyproject.toml
```

## 補足

依存パッケージを追加したい場合は、たとえば次のように実行します。

```bash
uv add requests
```
