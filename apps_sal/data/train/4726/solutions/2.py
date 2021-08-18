def solve(s):
    M = 10 ** 9 + 7
    z = ord('Z')
    base = z - ord('A') + 1

    left, total = 0, 0
    for c_num in [(z - ord(c)) for c in s]:
        l, t = left, total
        left = (l * base + c_num) % M
        total = ((l + 1) * c_num + t) % M
    return total
