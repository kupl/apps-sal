def palindrome(num, s):
    if type(123) != type(num) or type(123) != type(s):
        return 'Not valid'
    n = str(num)
    if any((not c.isdigit() for c in n)) or s < 0:
        return 'Not valid'
    R = []
    while len(R) < s:
        l = len(n)
        if num > 9 and all((a == b for (a, b) in zip(n[:l // 2], n[::-1]))):
            R.append(num)
        num += 1
        n = str(num)
    return R
