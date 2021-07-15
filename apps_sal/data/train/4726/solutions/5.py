def solve(s):
    a, pa = 0, 0
    for c in s:
        diff = ord('Z')-ord(c)
        a = a + diff + pa*diff
        pa = diff + pa*26
        a, pa = a%1000000007, pa%1000000007
    return a

