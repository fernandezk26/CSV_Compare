from itertools import zip_longest

#compares the the lines contained in two lists with dictionaries and returns the differences as a list
def compare_quotes(q1, q2):
    quote_differences= []
    for original_quote_lineItems, vendor_quote_lineItems in zip_longest(q1, q2, fillvalue = {}):
        if original_quote_lineItems !=  vendor_quote_lineItems:
            quote_differences.append(original_quote_lineItems)
    return quote_differences



