n = int(input())
a = input()
b = input()
ANS = 0
i = 0
while i < n:
    if a[i] == b[i]:
        i += 1
        continue
    if i + 1 < n and a[i + 1] != a[i] and (a[i] == b[i + 1]):
        ANS += 1
        i += 2
        continue
    else:
        ANS += 1
        i += 1
print(ANS)
