def palindrome(n, count):
    if not (isinstance(n, int) and isinstance(count, int)) or n < 0 or count < 0:
        return 'Not valid'
    result = []
    if n < 11:
        n = 11
    while count:
        s = str(n)
        if s == s[::-1]:
            result.append(n)
            count -= 1
        n += 1
    return result
