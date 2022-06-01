import csv
from datetime import date
from itertools import zip_longest

#reads two quotes and returns two lists containing dictionaries of line Items
def read_files(filePath1, filePath2):
    with open(filePath1, "r") as f:
        csv_reader = csv.DictReader(f)
        file1  = list(csv_reader)
        print(file1)

    with open(filePath2, "r") as f:
        csv_reader = csv.DictReader(f)
        file2  = list(csv_reader)
        print(file2)

    return file1, file2

#compares the the lines contained in two lists with dictionaries and returns the differences as a list
def compare_csv_files(file1, file2):
    file_differences= []
    for file1_lines, file2_lines in zip_longest(file1, file2, fillvalue = {}):
        if file1_lines !=  file2_lines:
            file_differences.append(file1_lines)
    return file_differences


#exports the differences to a new spreadsheet, along with the original info for reference
def export_file_differences(file1, file_differences, file2):
    #export the quotes and differences
    #Getting the Keys of the file to use as headers
    q1Keys = file1[0].keys()

    #set date and time info for csv file name
    today = date.today()
    filename = f"CSV_Comparison_Report_{str(today)}.csv"

    #setup and open the spreadsheet
    file1Header = ['CSV File 1']
    file2Header = ['CSV File 2']
    fileDifferencesHeader = ['File Differences']
    csvComparisonReport = open(filename, "w", newline='')
    quote_writer = csv.DictWriter(csvComparisonReport, q1Keys)
    writer = csv.writer(csvComparisonReport)

    #write the first file
    writer.writerow(file1Header)
    quote_writer.writeheader()
    quote_writer.writerows(file1)
    writer.writerow([])

    #write the second file
    writer.writerow(file2Header)
    quote_writer.writeheader()
    quote_writer.writerows(file2)
    writer.writerow([])

    #write the differences
    writer.writerow(fileDifferencesHeader)
    quote_writer.writeheader()
    quote_writer.writerows(file_differences)
