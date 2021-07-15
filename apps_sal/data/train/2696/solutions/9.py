def prime_string(s):
    for i in range(1,len(s) // 2 + 1):
        if len(s) % i == 0 and (len(s) // i) * s[:i] == s:
            return False
    return True
