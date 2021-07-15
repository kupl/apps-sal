def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]
