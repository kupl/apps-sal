def solve(s, z=ord('Z')):
    a = r = 0
    for i in (z - ord(c) for c in s):
        r += (a + 1) * i
        a = a * 26 + i
        r %= 1000000007
        a %= 1000000007
    return r
