import quoteComparisonFunctions as qc
import csvFunctions as c

# initializing list  
orderInformation = {"Order Number": "12345", "Date": "04/22/22", "Customer PO #" : "1234-5678"}

#read the quotes
readQuotesResult = c.readQuotes(q1FilePath="./testFiles/vendor.csv", q2FilePath="./testFiles/original.csv")
vendorQuote, originalQuote = readQuotesResult

#compare the quotes
quote_differences = qc.compareQuotes(q1 = vendorQuote, q2 = originalQuote)

#export the results
c.exportQuoteDifferences(orderInformation=orderInformation, originalQuote=originalQuote, vendorQuote=vendorQuote, quote_differences=quote_differences)