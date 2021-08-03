from sys import stdin
MODULO = 1000000007
for testcase in range(int(stdin.readline().strip())):
    s = stdin.readline().strip()
    s0 = (ord(s[0]) - 96) * 100
    wsum = sum([ord(ch) - 97 for ch in s]) + s0 * len(s)
    print(wsum % MODULO)
