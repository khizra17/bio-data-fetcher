# src/parsers.py
from io import StringIO
from Bio import SeqIO

def parse_fasta_to_summary(fasta_text):
    """
    Given FASTA text, return a summary dict for the first record:
    {id, description, length}
    """
    fh = StringIO(fasta_text)
    records = list(SeqIO.parse(fh, "fasta"))
    if not records:
        return {"id": None, "description": None, "length": 0}
    rec = records[0]
    return {"id": rec.id, "description": rec.description, "length": len(rec.seq)}
