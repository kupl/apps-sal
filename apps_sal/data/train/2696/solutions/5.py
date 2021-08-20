def prime_string(s):
    l = len(s)
    return not any((s == s[:l // n] * n for n in range(2, l + 1) if l % n == 0))
