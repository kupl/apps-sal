def is_good(n, awesome):
    return n in awesome or str(n) in '1234567890 9876543210' or str(n) == str(n)[::-1] or (int(str(n)[1:]) == 0)


def is_interesting(n, awesome):
    if n > 99 and is_good(n, awesome):
        return 2
    if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
        return 1
    return 0
