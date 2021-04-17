# CSV MASTER
Convert  [.CSV](https://tools.ietf.org/html/rfc4180) to any format ~

Supported formats (2):
 - [.XLSX](https://docs.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/) 👉 [jump](https://github.com/beastoin/csv-master#to-xlsx)
 - [.CSV Utf8 Sig (BOM)](https://tools.ietf.org/html/rfc3629#section-6) 👉 [jump](https://github.com/beastoin/csv-master#to-csv-utf8-sig-utf8-bom)

## To .XLSX
### Prerequisites
 - [python 2+](https://www.python.org/downloads)
 - [pip](https://pip.pypa.io/en/stable/installing/)

### Run

1. Open command line tool, e.g Terminal, Powershell

2. Run command:

 - For single file convert:

  ```
   python csv_xlsx.py -i <PATH/TO/CSV> -o <PATH/TO/OUTPUT/XLSX>
 ```
   > Example: `python csv_xlsx.py -i ~/Downloads/my-sample.csv -o my-sample.xlsx`

 - For multiple files convert:

  ```
  python csv_xlsx_bulk.py -i <PATH/TO/CSV/FOLDER>
 ```
   > Example: `python csv_xlsx_bulk.py -i ~/Downloads/my-csv-folder/`
  - NOTICE: Input folder path must end with `/` character
  - The .xlsx files will be located in the same folder with the .csv files

## To .CSV Utf8-Sig (Utf8 BOM)
### Prerequisites
 - [python 2+](https://www.python.org/downloads)
 - [pip](https://pip.pypa.io/en/stable/installing/)

### Run

1. Open command line tool, e.g Terminal, Powershell

2. Run command:

 - For single file convert:

  ```
   python csv_utf8sig.py -i <PATH/TO/CSV> -o <PATH/TO/OUTPUT/CSV>
 ```
   > Example: `python csv_utf8sig.py -i ~/Downloads/my-sample.csv -o my-sample.utf8sig.csv`

 - For multiple files convert:

  ```
  python csv_utf8sig_bulk.py -i <PATH/TO/CSV/FOLDER>
 ```
   > Example: `python csv_utf8sig_bulk.py -i ~/Downloads/my-csv-folder/`
  - NOTICE: Input folder path must end with `/` character
  - The .csv (.utf8sig.csv) files will be located in the same folder with the .csv files

## Troubleshootings
1. How to install python in Windows 10 pro?

 -> Please visit [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) and follow the instructions

2. `ModuleNotFoundError: No module named 'openpyxl'`

 -> Install module openpyxl via [pip](https://pip.pypa.io/en/stable/installing/): `pip install openpyxl`
 
3. `ModuleNotFoundError: No module named 'pandas'`

 -> Install module pandas via [pip](https://pip.pypa.io/en/stable/installing/): `pip install pandas`

