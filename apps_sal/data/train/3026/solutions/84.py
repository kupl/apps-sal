def min_value(digits):
    digitsSet = set(digits)
    listDigits = list(digitsSet)
    listDigits.sort()
    ans = str(list(listDigits)).replace('[', '').replace(']', '').replace(', ', '')
    return int(ans)
