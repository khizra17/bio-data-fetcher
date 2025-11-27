# src/fetchers/ensembl_fetcher.py
import requests
import time

ENSEMBL_REST = "https://rest.ensembl.org"

class EnsemblFetcher:
    def get_sequence(self, ensembl_id, retries=2, delay=1.0, seq_type="genomic"):
        seq_type_map = {"genomic": "", "cdna": "?type=cdna", "cds": "?type=cds", "protein": "?type=protein"}
        param = seq_type_map.get(seq_type, "")
        url = f"{ENSEMBL_REST}/sequence/id/{ensembl_id}{param}"
        headers = {"Accept": "text/plain", "Content-Type": "text/plain"}
        for attempt in range(retries + 1):
            try:
                r = requests.get(url, headers=headers, timeout=15)
                if r.status_code == 200:
                    text = r.text.strip()
                    if not text.startswith(">"):
                        return f">{ensembl_id}\n{text}"
                    return text
                elif r.status_code == 429:
                    retry_after = int(r.headers.get("Retry-After", delay))
                    time.sleep(retry_after)
                else:
                    r.raise_for_status()
            except Exception as exc:
                if attempt < retries:
                    time.sleep(delay)
                else:
                    raise RuntimeError(f"Ensembl fetch failed for {ensembl_id}: {exc}")
