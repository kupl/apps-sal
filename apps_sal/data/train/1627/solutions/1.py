from itertools import count

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def convert_digits(s):
    # converts each digit in base b in string s to its corresponding value in base 10
    # @return list of integers from 0 to b-1
    return [int(digits.index(d)) for d in s]

def convert_to_base_10(s,b):
    # converts an integer in base b to base 10
    # @input string representing integer and integer b representing base
    # @return string representing integer in base 10
    if b == 10:
        return s
    coeffs = convert_digits(s)[::-1]
    return str(sum([coeffs[i]*b**i for i in range(len(s))]))

def convert_from_base_10(s,b):
    #converts an integer from base 10 to base b
    # @input string representing integer and integer b representing base
    # @return string representing integer in base b
    max_exp = 0
    n = int(s)
    coeffs = []
    while b**(max_exp+1) <= n:
        max_exp += 1
    for k in range(max_exp+1):
        coeffs.append(digits[n%b])
        n = int((n-n%b)/b)
    return "".join(coeffs[::-1])

def is_polydivisible(s,b):
    # checks for polydivisibility in base b
    base_b = [s[:k] for k in range(1,len(s)+1)]
    #print("base_b = " + str(base_b))
    base10 = list(map(lambda s: convert_to_base_10(s,b), base_b))
    #print("base10 = " + str(base10))
    divisible = [int(base10[k])%(k+1) == 0 for k in range(1,len(s))]
    return not (False in divisible)

def get_polydivisible(n, b):
    # @return the nth polydivisible number in base b
    poly_count = 0
    for k in count(start=0, step=1):
        if is_polydivisible(convert_from_base_10(str(k),b), b):
            temp = str(k)
            poly_count += 1
            if poly_count == n:
                return convert_from_base_10(temp,b)
