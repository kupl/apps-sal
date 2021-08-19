def min_value(digits):
    s = ''
    ans = []
    digits.sort()
    new_digits = set(digits)
    for i in new_digits:
        ans.append(i)
    ans.sort()
    for i in ans:
        s += str(i)
    return int(s)
