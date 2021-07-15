def solve(s):
    r, l = 0, 0
    for c in s:
        m = ord('Z') - ord(c)
        r, l = r + m + l * m, m + l * 26
    return r % 1000000007
