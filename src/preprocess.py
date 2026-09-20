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


# loading

def load_bt():
    # header line starts with "# " so skip it and name the cols
    return pd.read_csv(
        RAW / "bt_symmetric.csv",
        skiprows=1,
        names=["timestamp", "user_a", "user_b", "rssi"],
        dtype={"timestamp": "int32", "user_a": "int16", "user_b": "int16", "rssi": "int8"}
    )
    
def load_fb():
    return pd.read_csv(
        RAW / "fb_friends.csv",
        skiprows=1, names=["user_a", "user_b"], dtype="int16"
    )


def load_calls():
    return pd.read_csv(
        RAW / "calls.csv",
        dtype={"timestamp": "int32", "caller": "int16", "callee": "int16", "duration": "int32"},
    )


def load_sms():
    return pd.read_csv(
        RAW / "sms.csv",
        dtype={"timestamp": "int32", "sender": "int16", "recipient": "int16"}
    )