Bio Data Fetcher – Full Automation Suite

A professional, production-grade automation suite for fetching biological sequence data from:

NCBI

Ensembl

UniProt

The suite automatically:

✔ Fetches raw sequence data
✔ Parses & cleans it
✔ Saves FASTA + summary CSV
✔ Runs standalone from CLI
✔ Supports multiple workers
✔ Includes clean modular architecture

Perfect for research workflows, automation pipelines, and bioinformatics projects.

🚀 Features
Data Fetchers

Each fetcher is fully modular and independently testable:

NCBI Fetcher – sequence retrieval via IDs (GenBank, RefSeq, etc.)

Ensembl Fetcher – gene/transcript/protein FASTA retrieval

UniProt Fetcher – SwissProt/UniProtKB sequences

Pipeline Automation

The pipeline:

Processes any number of IDs

Tries all fetchers automatically

Saves ALL results to outputs/

Produces a clean summary CSV

CLI Support

Run it like:

python -m src.cli --csv examples/sample_ids.csv --workers 4


Or:

python -m src.pipeline --input examples/sample_ids.csv --outdir outputs

📁 Project Structure
bio-data-fetcher/
│
├── src/
│   ├── fetchers/
│   │   ├── ncbi_fetcher.py
│   │   ├── ensembl_fetcher.py
│   │   └── uniprot_fetcher.py
│   ├── cli.py
│   ├── pipeline.py
│   └── utils.py
│
├── examples/
│   └── sample_ids.csv
│
├── outputs/        ← created after pipeline run
├── requirements.txt
└── README.md

🔧 Installation
1️⃣ Create a virtual environment
python -m venv venv

2️⃣ Activate it

Windows

venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶ How to Run
Run using CLI module
python -m src.cli --csv examples/sample_ids.csv --workers 2

Run using the unified pipeline
python -m src.pipeline --input examples/sample_ids.csv --outdir outputs

📊 Output Example

summary.csv will contain:

id	status	source	path	description	length	error
ENSG00000139618	downloaded	Ensembl	outputs/...fasta	BRCA2 gene	85183	
sp|P01308|INS	downloaded	UniProt	outputs/...fasta	Insulin protein	110	
NM_001126112	error	—	—	—	—	All fetchers failed
📌 Environment Variables (Optional)

Create .env:

NCBI_EMAIL=your_email@example.com

🏗 Future Enhancements

Add GENCODE fetcher

Add JSON metadata export

GUI control panel

Batch parallelization optimizations

🤝 Contributions

Feel free to fork, submit issues, or contribute enhancements.

🧪 Author

Khizra Nasir
Bioinformatics Automation Engineer
Project: Bio Data Fetcher – Professional Automation Suite