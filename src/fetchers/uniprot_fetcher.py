# src/fetchers/uniprot_fetcher.py
import requests
import time

UNIPROT_URL = "https://rest.uniprot.org/uniprotkb"

class UniProtFetcher:
    """Simple Uniprot sequence fetcher (returns FASTA-like)."""

    def get_fasta(self, uniprot_id, retries=2, delay=1.0):
        url = f"{UNIPROT_URL}/{uniprot_id}.fasta"
        headers = {"Accept": "text/plain"}
        for attempt in range(retries + 1):
            try:
                r = requests.get(url, headers=headers, timeout=15)
                if r.status_code == 200:
                    return r.text
                elif r.status_code == 429:
                    retry_after = int(r.headers.get("Retry-After", delay))
                    time.sleep(retry_after)
                else:
                    r.raise_for_status()
            except Exception as exc:
                if attempt < retries:
                    time.sleep(delay)
                else:
                    raise RuntimeError(f"UniProt fetch failed for {uniprot_id}: {exc}")
