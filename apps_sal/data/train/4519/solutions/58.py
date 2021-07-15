def max_number(n):
    s = [i for i in str(n)]
    s.sort()
    return int(''.join(i for i in s[::-1]))
