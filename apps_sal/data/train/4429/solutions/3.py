def longest_palindrome(s):
    new_s = ''.join([x for x in s.lower() if x.isalnum()])
    k = [new_s.count(x) for x in set(new_s)]

    res = 0
    for x in k:
        if x % 2 == 0:
            res += x
        else:
            res += (x - 1)

    return res + 1 if any(x % 2 == 1 for x in k) else res
