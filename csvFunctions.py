import csv
from datetime import date
#reads two quotes and returns two lists containing dictionaries of line Items
def readQuotes(q1FilePath, q2FilePath):
    with open(q1FilePath, "r") as f:
        csv_reader = csv.DictReader(f)
        vendorQuote  = list(csv_reader)
        print(vendorQuote)

    with open(q2FilePath, "r") as f:
        csv_reader = csv.DictReader(f)
        originalQuote  = list(csv_reader)
        print(originalQuote)
    
    return vendorQuote, originalQuote


def exportQuoteDifferences(originalQuote, orderInformation, quote_differences, vendorQuote):
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
