import os
from os import listdir
from os.path import isfile, join
import csv
from openpyxl import Workbook

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

    wb = Workbook()
    ws = wb.active
    with open(path, 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save(out)

    print("  -> DONE")
