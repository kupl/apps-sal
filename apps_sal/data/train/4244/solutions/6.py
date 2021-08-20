def palindrome(num):
    s = str(num)
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    return num > 9 and sum((s.count(x) % 2 for x in set(s))) < 2
