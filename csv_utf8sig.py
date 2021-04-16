import argparse
import csv
import pandas as pd

# Command-line args parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help=".xlsx input file path")
parser.add_argument("-o", "--output", help=".csv utf8-sig output file path")

# Parse command line
args = parser.parse_args()

# Input
path =  args.input
out = args.output

print("CONVERTING...", path)
print("  ->", out)

df = pd.read_csv(path, encoding='utf-8')
df.to_csv(out, encoding='utf-8-sig', index=False)

print("  -> DONE")
