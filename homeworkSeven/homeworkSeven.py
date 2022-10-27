# Lilia Bodnar
# Lab 7
# 10272022

import pandas as pd
from pathlib import Path

datapath = Path("data") / "city_temperature.csv"
df = pd.read_csv(datapath, sep=",")
print(df)