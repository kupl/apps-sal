def permute_a_palindrome(input):
    res = 0
    for c in input.lower():
        res = res ^ 1 << ord(c) - 71
    return res == res & -res
