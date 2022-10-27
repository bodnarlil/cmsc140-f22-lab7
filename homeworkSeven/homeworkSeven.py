# Lilia Bodnar
# Lab 7
# 10272022
# Region,Country,State,Month,Day,Year,AvgTemperature

import pandas as pd
from pathlib import Path

datapath = Path("data") / "city_temperature.csv"
df = pd.read_csv(datapath, sep=",")
print(df)

df.groupby(['Region'])
print(df)

# create a new CSV called outfile
outfile = Path("data") / "cityTempsEdited.csv"

# create a for loop that finds the max
regionMax = 0
for region in df:
    for line in region:
        if(region["AvgTemperature"] > regionMax ):
            regionMax = region["AvgTemperature"]
            # add the row to the csv file
            outfile["highestTemp"] = outfile.apply(lambda row: region, axis = 1)
    # reset the region max to 0
    regionMax = 0

# save the csv
df.to_csv(outfile, index_label="index")