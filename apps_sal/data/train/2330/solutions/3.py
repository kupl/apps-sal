s = input()
n = len(s)
f = 1
if s[-1] == "1":
    f = 0
if s[0] == "0":
    f = 0
for i in range(n - 1):
    if s[i] != s[-2 - i]:
        f = 0
        break

s = s[:-1] + "1"
if f:
    k = 0
    for i in range(n):
        if s[i] == "1":
            for j in range(k, i):
                print(j + 1, i + 1)
            k = i
else:
    print(-1)
