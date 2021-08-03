def f(s, symb):
    if len(s) == 1:
        return int(s[0] != symb)
    f1 = f2 = 0
    c1 = ''
    c2 = ''
    for i in range(len(s) // 2):
        f1 += int(s[i] != symb)
        c1 += s[i]
    for i in range(len(s) // 2, len(s)):
        f2 += int(s[i] != symb)
        c2 += s[i]
    ns = chr(ord(symb) + 1)
    return min(f1 + f(c2, ns), f2 + f(c1, ns))


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(f(s, 'a'))
