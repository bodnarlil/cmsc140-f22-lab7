# Lilia Bodnar
# Lab 7
# 10272022

# get all the basic stuff and organize it by region
import pandas as pd
from pathlib import Path
datapath = Path("city_temperature.csv")
df = pd.read_csv(datapath, sep=",")
newGrouping = pd.read_csv(datapath, sep=",").groupby(['Region'])

# find the max using idmax from the notes with the baseball.txt
maxTempsRegion = newGrouping["AvgTemperature"].idxmax()
maxTemps = df.loc[maxTempsRegion]

# create the outfile and save the csv in the same line
maxTemps.to_csv(Path("city_maxtemp.csv"), index = False)