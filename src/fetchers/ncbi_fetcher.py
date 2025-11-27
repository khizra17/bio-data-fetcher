# src/fetchers/ncbi_fetcher.py
from Bio import Entrez
import time
from pathlib import Path
from ..utils import get_env

# configure Entrez from .env
ENTREZ_EMAIL = get_env("ENTREZ_EMAIL", "your_email@example.com")
ENTREZ_API_KEY = get_env("ENTREZ_API_KEY", "")
Entrez.email = ENTREZ_EMAIL
if ENTREZ_API_KEY:
    Entrez.api_key = ENTREZ_API_KEY

class NCBIFetcher:
    """Fetcher for NCBI nucleotide FASTA using Biopython Entrez.efetch"""

    def fetch_fasta(self, accession, retries=2, delay=1.0):
        for attempt in range(retries + 1):
            try:
                handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
                fasta = handle.read()
                handle.close()
                if not fasta or not fasta.strip():
                    raise ValueError("Empty FASTA returned")
                return fasta
            except Exception as exc:
                if attempt < retries:
                    time.sleep(delay)
                else:
                    raise RuntimeError(f"NCBI fetch failed for {accession}: {exc}")
