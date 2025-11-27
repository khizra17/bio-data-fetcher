# src/worker.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from .pipeline import Pipeline
from .db.cache import init_db
from pathlib import Path
from tqdm import tqdm

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def run_batch(ids, max_workers=4):
    init_db()
    pipeline = Pipeline()
    results = []
    ids = list(dict.fromkeys(ids))
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(pipeline.fetch_and_process, id_): id_ for id_ in ids}
        for fut in tqdm(as_completed(futures), total=len(futures)):
            id_ = futures[fut]
            try:
                results.append(fut.result())
            except Exception as exc:
                results.append({"id": id_, "status": "error", "error": str(exc)})
    return results
