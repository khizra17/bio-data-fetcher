# src/cli.py
import argparse
from pathlib import Path
import csv
from .worker import run_batch
from .db.cache import init_db

def read_ids_from_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    ids = []
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.reader(fh):
            if not row:
                continue
            val = row[0].strip()
            if val:
                ids.append(val)
    return ids

def save_summary(results, path):
    import pandas as pd
    df = pd.DataFrame(results)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path

def main():
    parser = argparse.ArgumentParser(description="BioData Fetcher CLI")
    parser.add_argument("--ids", nargs="+", help="One or more accession/ensembl/uniprot ids")
    parser.add_argument("--csv", help="CSV file with one id per line")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers")
    parser.add_argument("--summary", default="outputs/summary.csv", help="Path for CSV summary")
    args = parser.parse_args()

    init_db()

    ids = []
    if args.ids:
        ids.extend(args.ids)
    if args.csv:
        ids.extend(read_ids_from_csv(args.csv))

    if not ids:
        print("No IDs provided. Use --ids or --csv")
        return

    print(f"Running batch for {len(ids)} ids with {args.workers} workers...")
    results = run_batch(ids, max_workers=args.workers)
    summary_path = save_summary(results, args.summary)
    print(f"Done. Summary saved to: {summary_path}")

if __name__ == "__main__":
    main()
