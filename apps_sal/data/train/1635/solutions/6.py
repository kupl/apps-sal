from math import factorial

# on factorial number system and its relation to lexicographically ordered permutations;
# https://medium.com/@aiswaryamathur/find-the-n-th-permutation-of-an-ordered-string-using-factorial-number-system-9c81e34ab0c8
# https://en.wikipedia.org/wiki/Factorial_number_system
def factoradic_representation(n):
    res = []
    i = 1
    while n > 0:
        res.append(n % i)
        n = n // i
        i += 1
    return res[::-1]

def middle_permutation(string):
    if len(string) < 2:
        return string
    s = sorted(string)
    res = []
    fr = factoradic_representation(factorial(len(s))//2-1)
    fr = [0] * (len(string) - len(fr)) + fr
    for idx in fr:
        res.append(s.pop(idx))
    return "".join(res)
