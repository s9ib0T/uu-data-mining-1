# uu-data-mining-1

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
scripts/download.sh
```

`scripts/download.sh` downloads the Copenhagen Networks Study data from figshare to `data/copenhagen/`. It skips files that already exist. The first code cell in `notebooks/preprocess.ipynb` runs the same script.

Do not edit the files in `data/copenhagen/`. Save changed data to `data/processed/`.
