def palindrome(n, s, r=[]):
    if not isinstance(n, int) or not isinstance(s, int) or n < 0 or s < 0:
        return "Not valid"

    while len(r) < s:
        n, s, r = n + 1, s, r + [n] if str(n) == str(n)[::-1] and n > 9 else r

    return r
