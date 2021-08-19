def is_palindrome(s):
    # If s is an int, make a list of digits of it
    if isinstance(s, int):
        digits = []
        while s:
            s, r = divmod(s, 10)
            digits.append(r)
        s = digits

    # Now check if the left side of s is the reversed of the right side
    return all(s[l] == s[r] for l, r in enumerate(range(len(s) - 1, len(s) // 2 - 1, -1)))
