d = input().split()

n = int(d[0])
m = int(d[1])

r = 0
q = 0

for i in range(m):
    s = [int(x) for x in input().split()][1::]
    if s[0] != 1:
        r += len(s) - 1
        q += len(s)
    else:
        if len(s) <= 1:
            q += 1
        else:
            w = 0
            while w+1 < len(s) and s[w] == s[w+1] - 1:
                w += 1
            q += len(s) - w
            r += len(s) - w - 1

print(r + q - 1)
