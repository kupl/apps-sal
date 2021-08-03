t = int(input())
for _ in range(t):
    s = input()
    l = len(s)
    d, j = 0, 0
    for i in range(l - 1, -1, -1):
        if s[i] == 'A':
            d += 10 * 16**j
        elif s[i] == 'B':
            d += 11 * 16**j
        elif s[i] == 'C':
            d += 12 * 16**j
        elif s[i] == 'D':
            d += 13 * 16**j
        elif s[i] == 'E':
            d += 14 * 16**j
        elif s[i] == 'F':
            d += 15 * 16**j
        else:
            d += int(s[i]) * 16**j
        j += 1
    print(d)
