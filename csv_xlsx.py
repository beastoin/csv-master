import argparse
import csv
from openpyxl import Workbook

# Command-line args parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help=".csv input file path")
parser.add_argument("-o", "--output", help=".xlsx output file path")

# Parse command line
args = parser.parse_args()

# Input
path =  args.input
out = args.output

print("CONVERTING...", path)
print("  ->", out)

wb = Workbook()
ws = wb.active
with open(path, 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save(out)

print("  -> DONE")
