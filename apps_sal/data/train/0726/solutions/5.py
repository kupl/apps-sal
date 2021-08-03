n = int(input())
for i in range(n):
    n1 = int(input())
    c, o, d, e, h, f = 0, 0, 0, 0, 0, 0
    for j in range(n1):

        s = input()
        for k in range(len(s)):
            if s[k] == "c":
                c += 1
            elif s[k] == "o":
                o += 1
            elif s[k] == "d":
                d += 1
            elif s[k] == "e":
                e += 1
            elif s[k] == "h":
                h += 1
            elif s[k] == "f":
                f += 1

    c /= 2
    e /= 2

    print(int(min(c, o, d, e, h, f)))
