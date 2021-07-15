geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

# given an array of strings, return a new array removing strings found in geese
# The elements in the returned array should be in the same order as in the initial array passed to your function
# some elements may be repeated and all will be in the same case

# input - array of strings
# output - array of strings

def goose_filter(birds):
# return element in birds if element is not in geese
    return [x for x in birds if x not in geese]
