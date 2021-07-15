s = input()
if s[0] == "0" or s[-1] == "1":
    print((-1))
    return
n = len(s)
if n == 2:
    if s == "10":
        print((1, 2))
        return
    else:
        print((-1))
        return

m = n // 2
tmp = m + 1
ANS = []
for i in reversed(list(range(1, m + 1))):
    j = n - i
    if s[i - 1] == "1" and s[j - 1] == "1":
        ANS.append((tmp, i))
        tmp = i
    elif s[i - 1] == "0" and s[j - 1] == "0":
        ANS.append((tmp, i))
    else:
        print((-1))
        return
for i in range(m + 2, n + 1):
    ANS.append((m + 1, i))

for a, b in ANS:
    print((a, b))

