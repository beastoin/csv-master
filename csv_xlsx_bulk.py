import os
from os import listdir
from os.path import isfile, join

import csv

from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from pandas.io.excel import ExcelWriter
import pandas

import argparse

# Command-line args parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help=".csv input folder path. Required postfix /")

# Parse command line
args = parser.parse_args()

mypath = args.input
files = [f for f in listdir(mypath) if isfile(join(mypath, f)) & f.endswith(".csv")]
for x in files:
    path = mypath + x
    out = mypath + x + ".xlsx"

    print("CONVERTING...", path)
    print("  ->", out)

    with ExcelWriter(out) as ew:
        df = pandas.read_csv(path, encoding='utf8')
        df = df.replace(to_replace=ILLEGAL_CHARACTERS_RE, value='', regex=True)
        df.to_excel(ew, sheet_name="Sheet1", index=False)

    print("  -> DONE")
