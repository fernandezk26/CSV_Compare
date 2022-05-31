import csv
from datetime import date
import quoteComparisonFunctions as qc

# initializing list 
orderInformation = {"Order Number": "12345", "Date": "04/22/22", "Customer PO #" : "1234-5678"}

#read the quotes
test = qc.readQuotes(q1FilePath="./testFiles/vendor.csv", q2FilePath="./testFiles/original.csv")
vendorQuote, originalQuote = test

#compare the quotes
quote_differences = qc.compareQuotes(q1 = vendorQuote, q2 = originalQuote)

#export the quotes and differences
#Getting the Keys of the file to use as headers
q1Keys = originalQuote[0].keys()
orderKeys = orderInformation.keys()

#set date and time info for csv file name
today = date.today()
filename = f"Quote_Comparison_Report_{str(today)}.csv"

#setup and open the spreadsheet
orderInformationHeader = ['Order Information']
originalQuoteHeader = ['Original Quote']
vendorQuoteHeader = ['Vendor Quote']
quoteDifferencesHeader = ['Quote Differences']
quoteComparisonReport = open(filename, "w", newline='')
quote_writer = csv.DictWriter(quoteComparisonReport, q1Keys)
order_writer = csv.DictWriter(quoteComparisonReport, orderKeys)
writer = csv.writer(quoteComparisonReport)

#write order information
writer.writerow(orderInformationHeader)
order_writer.writeheader()
order_writer.writerow(orderInformation)
writer.writerow([])

#write the first quote
writer.writerow(originalQuoteHeader)
quote_writer.writeheader()
quote_writer.writerows(originalQuote)
writer.writerow([])

#write the second quote
writer.writerow(vendorQuoteHeader)
quote_writer.writeheader()
quote_writer.writerows(vendorQuote)
writer.writerow([])

#write the differences
writer.writerow(quoteDifferencesHeader)
quote_writer.writeheader()
quote_writer.writerows(quote_differences)