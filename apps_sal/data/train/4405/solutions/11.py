def is_palindrome(s):
    if isinstance(s, int):
        digits = []
        while s:
            (s, r) = divmod(s, 10)
            digits.append(r)
        s = digits
    return all((s[l] == s[r] for (l, r) in enumerate(range(len(s) - 1, len(s) // 2 - 1, -1))))
