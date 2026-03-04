# AgentsTest01
AIAgent利用プロジェクトのテスト用です

## analyze.py の使い方

### 実行コマンド例

```bash
python analyze.py --input sample.csv
python analyze.py --input sample.tsv
```

### 入力フォーマット

- 1行目はヘッダー（列名）
- 2行目以降にデータ
- `sample.csv` はカンマ区切り、`sample.tsv` はタブ区切り
- 数値として解釈できるセルのみ集計対象（空欄や文字列は無視）

例（CSV）:

```csv
name,score,height
Alice,80,160.5
Bob,90,172.0
Carol,85,168.2
```

実行すると、数値が含まれる各列ごとに以下の統計値を標準出力に表示します。

- 件数（count）
- 平均（mean）
- 中央値（median）
- 最小値（min）
- 最大値（max）
