Bio Data Fetcher – Full Automation Suite

A professional, production-grade automation suite for fetching biological sequence data from multiple authoritative sources:

NCBI

Ensembl

UniProt

This toolkit automates the complete workflow:

✔ Fetches biological sequences
✔ Cleans & parses data
✔ Saves FASTA + summary CSV
✔ Runs as a standalone CLI tool
✔ Supports parallel workers
✔ Built with clean, modular architecture

Perfect for researchers, bioinformatics engineers, automation pipelines, and academic workflows.

🚀 Features
🔬 Multi-Source Data Fetchers

Each fetcher is fully modular, independently testable, and follows a unified interface:

NCBI Fetcher
Retrieves GenBank/RefSeq sequences using accession IDs.

Ensembl Fetcher
Fetches gene, transcript, or protein FASTA files.

UniProt Fetcher
Retrieves curated SwissProt/UniProtKB protein sequences.

⚙️ Automated Pipeline

The unified pipeline:

Processes any number of IDs

Automatically tries all fetchers for each ID

Saves FASTA outputs into /outputs

Generates a clean summary.csv report

Runs with multi-threading (--workers)

💻 Command Line Interface (CLI)

Run via the CLI module:

python -m src.cli --csv examples/sample_ids.csv --workers 4


Or use the full automation pipeline:

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
├── outputs/        ← created automatically after running the pipeline
│
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
Using the CLI
python -m src.cli --csv examples/sample_ids.csv --workers 2

Using the unified pipeline
python -m src.pipeline --input examples/sample_ids.csv --outdir outputs

📊 Example Output (summary.csv)
id	status	source	path	description	length	error
ENSG00000139618	downloaded	Ensembl	outputs/...fasta	BRCA2 gene	85183	
sp|P01308|INS	downloaded	UniProt	outputs/...fasta	Insulin protein	110	
NM_001126112	error	—	—	—	—	All fetchers failed
🔐 Optional Environment Variable

Create a .env file:

NCBI_EMAIL=your_email@example.com

🏗 Planned Enhancements

GENCODE fetcher

JSON metadata export

GUI dashboard / control panel

Faster batch parallelization

🤝 Contributions

Contributions, issues, and pull requests are welcome.
Feel free to fork and enhance the automation suite.

🧪 Author

Khizra Nasir
Bioinformatics Automation Engineer
Project: Bio Data Fetcher – Professional Automation Suite