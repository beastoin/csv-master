import argparse
import os
from os import listdir
from os.path import isfile, join
import csv
import pandas as pd

# Command-line args parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help=".csv input folder path. Required postfix /")

# Parse command line
args = parser.parse_args()

mypath = args.input
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) & f.endswith(".csv")]
for x in files:
    path = mypath + x
    out = mypath + x + ".utf8sig.csv"

    print("CONVERTING...", path)
    print("  ->", out)

    df = pd.read_csv(path, encoding='utf-8')
    df.to_csv(out, encoding='utf-8-sig', index=False)

    print("  -> DONE")
