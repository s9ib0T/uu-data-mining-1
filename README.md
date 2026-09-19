# uu-data-mining-1

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
scripts/download.sh
```

When opening a notebook, select `.venv/bin/python` as the kernel; the notebooks need the packages installed in `.venv`.

`scripts/download.sh` downloads the Copenhagen Networks Study data from figshare to `data/copenhagen/`. It skips files that already exist. The first code cell in `notebooks/preprocess.ipynb` runs the script.

Do not edit the files in `data/copenhagen/`. Save changed data to `data/processed/`.

Analysis code is in `src/`, and the notebooks import it.