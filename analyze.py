#!/usr/bin/env python3
"""CSV/TSV の数値列を集計するスクリプト。"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import median
from typing import Dict, List



def compute_stats(values: List[float]) -> Dict[str, float]:
    """数値配列の基本統計量を返す。"""
    if not values:
        raise ValueError("values must not be empty")

    return {
        "count": float(len(values)),
        "mean": sum(values) / len(values),
        "median": median(values),
        "min": min(values),
        "max": max(values),
    }



def infer_delimiter(path: Path) -> str:
    if path.suffix.lower() == ".tsv":
        return "\t"
    return ","



def read_numeric_columns(path: Path) -> Dict[str, List[float]]:
    delimiter = infer_delimiter(path)
    numeric_columns: Dict[str, List[float]] = {}

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        if not reader.fieldnames:
            return {}

        numeric_columns = {name: [] for name in reader.fieldnames}

        for row in reader:
            for col, raw in row.items():
                if raw is None:
                    continue
                value = raw.strip()
                if value == "":
                    continue
                try:
                    numeric_columns[col].append(float(value))
                except ValueError:
                    # 数値として解釈できない値は無視する
                    continue

    return {col: values for col, values in numeric_columns.items() if values}



def format_stats(column: str, stats: Dict[str, float]) -> str:
    return (
        f"[{column}]\n"
        f"  count  : {int(stats['count'])}\n"
        f"  mean   : {stats['mean']:.6g}\n"
        f"  median : {stats['median']:.6g}\n"
        f"  min    : {stats['min']:.6g}\n"
        f"  max    : {stats['max']:.6g}"
    )



def main() -> None:
    parser = argparse.ArgumentParser(description="CSV/TSV の数値列を分析します")
    parser.add_argument("--input", required=True, help="入力ファイルパス（CSV/TSV）")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"input file not found: {input_path}")

    columns = read_numeric_columns(input_path)
    if not columns:
        print("数値列が見つかりませんでした。")
        return

    for idx, (col, values) in enumerate(columns.items()):
        if idx > 0:
            print()
        print(format_stats(col, compute_stats(values)))


if __name__ == "__main__":
    main()
