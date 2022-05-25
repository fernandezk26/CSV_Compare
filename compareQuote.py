from ast import Pass
from asyncore import write
import csv
from  itertools import zip_longest
from datetime import date
import os

today = date.today()
filename = f"Quote_Comparison_Report_{str(today)}.csv"

# initializing list 
orderInformation = {"Order Number": "12345", "Date": "04/22/22", "Customer PO #" : "1234-5678"}

originalQuote = [
    {"Item Code": "K1234", "Item Description": "Jazzy chair E9999", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$5000", "Terms Disc/Unit": "$400", "Total Net Value": "$400"},
    {"Item Code": "Q6", "Item Description": "Leg Rest K0000", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "350", "Terms Disc/Unit": "$300", "Total Net Value": "$50"},
    {"Item Code": "J732", "Item Description": "Wheels E1234", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$20", "Terms Disc/Unit": "$10", "Total Net Value": "$10"},
    {"Item Code": "72-1234", "Item Description": "Cushion K0108", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$1000", "Terms Disc/Unit": "$500", "Total Net Value": "$500"},
    {"Item Code": "1234556", "Item Description": "Misc part K010", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$3", "Terms Disc/Unit": "$1", "Total Net Value": "$2"},
]

vendorQuote = [
    {"Item Code": "K1234", "Item Description": "Jazzy chair E9999", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$500", "Terms Disc/Unit": "$400", "Total Net Value": "$400"},
    {"Item Code": "Q6", "Item Description": "Leg Rest K0000", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "350", "Terms Disc/Unit": "$300", "Total Net Value": "$50"},
    # {"Item Code": "J732", "Item Description": "Wheels E1234", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$20", "Terms Disc/Unit": "$10", "Total Net Value": "$10"},
    {"Item Code": "72-1234", "Item Description": "Cushion K0108", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$1000", "Terms Disc/Unit": "$500", "Total Net Value": "$500"},
    {"Item Code": "ITEM NOT IN QUOTE 1", "Item Description": "ITEM NOT IN QUOTE 1", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$1000", "Terms Disc/Unit": "$500", "Total Net Value": "$500"},
    # {"Item Code": "123455699", "Item Description": "Part on Quote 2 not on Quote 1", "Quantity Ordered": 1, "Quantity Shipped": 0, "Unit MSRP/Base Prov.": "$3", "Terms Disc/Unit": "$1", "Total Net Value": "$2"}
]


#iterate through the quotes and append any differences to a list
quote_differences= []
for original_quote_lineItems, vendor_quote_lineItems in zip_longest(vendorQuote, originalQuote, fillvalue = {}):
    if original_quote_lineItems !=  vendor_quote_lineItems:
        quote_differences.append(original_quote_lineItems)

#Getting the Keys of the file to use as headers
q1Keys = originalQuote[0].keys()
orderKeys = orderInformation.keys()

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