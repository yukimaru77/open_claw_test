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
uv run python minimal_uv_project.py
```

### エントリーポイントとして実行

```bash
uv run minimal-uv-project
```

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
