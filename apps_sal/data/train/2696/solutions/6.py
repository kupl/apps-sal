def prime_string(s):
    l = len(s)
    for i in range(1, len(s) // 2 + 1):
        a = s[:i]
        b = l // i
        if a * b == s:
            return False
    return True
