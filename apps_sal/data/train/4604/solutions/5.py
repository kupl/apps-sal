def palindrome(n):
    if not isinstance(n, int) or n < 0:
        return 'Not valid'
    s = f'{n}'
    return any((n in s[i:i + 2] for (i, n) in enumerate(s[:-1], 1)))
