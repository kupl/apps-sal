# n is the number of customers buying hotdogs
# input - integers
# output - integer, cost of hotdog

def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    else:
        return n * 90
