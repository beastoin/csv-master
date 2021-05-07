from pandas.io.excel import ExcelWriter
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
import pandas
import argparse
import csv

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

with ExcelWriter(out) as ew:
    df = pandas.read_csv(path, encoding='utf8')
    df = df.replace(to_replace=ILLEGAL_CHARACTERS_RE, value='', regex=True)
    df.to_excel(ew, sheet_name="Sheet1")

print("  -> DONE")
