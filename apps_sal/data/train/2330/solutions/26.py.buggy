s = list(input())
n = len(s)
if s[n - 1] == "1" or s[0] == "0":
    print(-1)
    return
for i in range((n - 1) // 2):
    if not s[i] == s[n - 2 - i]:
        print(-1)
        return
l = n - s.count("0") + 1
x = [0] * l
j = 0
for i in range(n // 2):
    if s[i] == "1":
        j += 1
    else:
        x[j] += 1
        x[l - 1 - j] += 1
        if j == l - 1 - j and n % 2 == 0 and i == (n - 1) // 2:
            x[j] -= 1
for i in range(l - 1):
    print(i + 1, i + 2)
k = n - s.count("0") + 2
for i in range(l):
    for _ in range(x[i]):
        print(i + 1, k)
        k += 1
