#Using Pandas Lib to merge Project Essay lists and Project Descriptions
import pandas as pd

#read in the two datasets
a = pd.read_csv("C:/Data/TextMining/Project/EssaysParsedFull.csv")
b = pd.read_csv("C:/Data/TextMining/Project/ProjectParsedFull.csv")

#merge on project ID and output to CSV
merged = a.merge(b, on='_projectid')
merged.to_csv("C:/Data/TextMining/Project/mergedFull.csv", index=False)

