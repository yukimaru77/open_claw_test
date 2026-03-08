# minimal-uv-project

`uv` を使った最小構成の Python プロジェクトです。

## 必要環境

- `uv`
- Python 3.11 以上

## セットアップ

```bash
uv sync
```

## 実行方法

### スクリプトとして実行

```bash
uv run python minimal_uv_project.py Alice --times 2
```

### エントリーポイントとして実行

```bash
uv run minimal-uv-project Alice --times 2
uv run minimal-uv-project Bob --uppercase
```

### ヘルプ表示

```bash
uv run minimal-uv-project --help
```

## CLI仕様

- `name`: あいさつする相手の名前（省略時は `uv`）
- `-t`, `--times`: あいさつを表示する回数
- `--uppercase`: あいさつを大文字で表示

## プロジェクト構成

```text
.
├── .gitignore
├── .python-version
├── README.md
├── minimal_uv_project.py
└── pyproject.toml
```

## 補足

依存パッケージを追加したい場合は、たとえば次のように実行します。

```bash
uv add requests
```
