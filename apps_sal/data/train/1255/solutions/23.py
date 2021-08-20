import string
for a in range(int(input())):
    (s, k) = input().split()
    k = int(k)
    if 26 - len(s) + k < len(s):
        print('NOPE')
    else:
        t = ''
        f = 0
        for c in string.ascii_lowercase:
            if c in s and f < k:
                t += c
                f += 1
            elif c not in s:
                t += c
            if len(t) == len(s):
                break
        print(t)
