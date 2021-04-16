# CSV MASTER
Convert csv to any format

## .XLSX
Prerequisite: [python 2+](https://www.python.org/downloads)

### RUN

1. Open command line tool, e.g Terminal, Powershell

2. Run command:

 - For single file convert:

  ```
 python csv_xlsx.py -i <PATH/TO/CSV> -o <PATH/TO/OUTPUT/XLSX
 ```

   > Example: `python csv_xlsx.py -i ~/Downloads/my-sample.csv -o my-sample.xlsx`

 - For multiple files convert:

  ```
 python csv_xlsx_bulk.py -i <PATH/TO/CSV/FOLDER>
 ```
  - NOTICE: Input folder must end with `/` character
   > Example: `python csv_xlsx_bulk.py -i ~/Downloads/my-csv-folder/`


### Troubleshotings
1. How to install python in Windows 10 pro?
 -> Please visit [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) and follow the instructions

