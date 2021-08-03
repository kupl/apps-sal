def has_subpattern(string):
    s = len(string)
    for i in range(1, s // 2 + 1):
        if s % i == 0:
            q = s // i
            if string[:i] * q == string:
                return True
    return False
