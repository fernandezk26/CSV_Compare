import csv_comparison_functions as c

#read the csv files
readFilesResult = c.read_files(filePath1="./testFiles/vendor.csv", filePath2="./testFiles/original.csv")
file1, file2 = readFilesResult

#compare the quotes
file_differences = c.compare_csv_files(file1 = file1, file2 = file2)

#export the results
c.export_quote_differences(file1=file1, file2=file2, file_differences=file_differences)