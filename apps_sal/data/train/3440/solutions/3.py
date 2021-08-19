# return an array of numbers (that are a power of 2)
# for which the input "n" is the sum
def powers(n):
    s = bin(n)[::-1]
    return [2**i for i, x in enumerate(s) if x == '1']
