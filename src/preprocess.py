from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent.parent
RAW = ROOT / "data" / "copenhagen"
PROCESSED = ROOT / "data" / "processed"

BIN = 300 # seconds between bluetooth scans
N_BINS = 8064 # 28 days of 5 minute bins
DAY = 86400 # seconds
EMPTY = -1 # user_b of an empty scan
OUTSIDE = -2 # user_b of a device outside the study

