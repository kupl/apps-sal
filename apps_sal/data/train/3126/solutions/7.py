def palindrome_rearranging(s):
    for c in s:
        if s.count(c) > 1:
            s = s.replace(c, "", 2)
    return len(s) < 2
