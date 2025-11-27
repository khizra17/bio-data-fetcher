# src/pipeline.py
from pathlib import Path
from .fetchers.ncbi_fetcher import NCBIFetcher
from .fetchers.ensembl_fetcher import EnsemblFetcher
from .fetchers.uniprot_fetcher import UniProtFetcher
from .parsers import parse_fasta_to_summary
from .db.cache import init_db, get_cached, cache_result
from .utils import ensure_dir
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
ensure_dir(OUTPUT_DIR)

class Pipeline:
    def __init__(self):
        init_db()
        self.ncbi = NCBIFetcher()
        self.ensembl = EnsemblFetcher()
        self.uniprot = UniProtFetcher()

    def fetch_and_process(self, identifier: str, source_hint: Optional[str]=None):
        """
        Try to fetch a sequence using a hint or fallback order:
        - if hint == "ensembl" / "uniprot" / "ncbi" use that first.
        - otherwise try NCBI -> Ensembl -> UniProt
        Returns a dict with metadata and where file was saved.
        """
        cached = get_cached(identifier)
        if cached:
            return {"id": identifier, "status": "cached", "source": cached[1], "path": cached[3]}

        fetchers = []
        if source_hint == "ensembl":
            fetchers = [self.ensembl.get_sequence]
        elif source_hint == "uniprot":
            fetchers = [self.uniprot.get_fasta]
        elif source_hint == "ncbi":
            fetchers = [self.ncbi.fetch_fasta]
        else:
            fetchers = [self.ncbi.fetch_fasta, self.ensembl.get_sequence, self.uniprot.get_fasta]

        for fn in fetchers:
            try:
                fasta = fn(identifier)
                # save to outputs
                filepath = OUTPUT_DIR / f"{identifier}.fasta"
                filepath.write_text(fasta, encoding="utf-8")
                # parse summary
                summary = parse_fasta_to_summary(fasta)
                cache_result(identifier, fn.__module__, filepath)
                return {"id": identifier, "status": "downloaded", "source": fn.__module__, "path": str(filepath), **summary}
            except Exception:
                continue

        return {"id": identifier, "status": "error", "error": "All fetchers failed"}
