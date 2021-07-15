def luck_check(s):
    if not s or not all(c in '0123456789' for c in s):
        raise ValueError('Invalid ticket number')
    e0, b1 = len(s) // 2, (len(s) + 1) // 2
    return sum(map(int, s[:e0])) == sum(map(int, s[b1:]))
