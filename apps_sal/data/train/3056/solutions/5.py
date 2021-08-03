def palindrome(num, s):
    if isinstance(num, str) or num < 0 or isinstance(s, str) or s < 0:
        return 'Not valid'
    t = []
    i = 1
    while i <= s:
        if pali(num):
            t.append(num)
            i += 1
        num += 1
    return t


def pali(n):
    if n > 10 and str(n) == str(n)[::-1]:
        return True
    return False
