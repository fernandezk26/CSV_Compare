import csv
from itertools import zip_longest

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

#compares the the lines contained in two lists with dictionaries and returns the differences as a list
def compareQuotes(q1, q2):
    quote_differences= []
    for original_quote_lineItems, vendor_quote_lineItems in zip_longest(q1, q2, fillvalue = {}):
        if original_quote_lineItems !=  vendor_quote_lineItems:
            quote_differences.append(original_quote_lineItems)
    return quote_differences



