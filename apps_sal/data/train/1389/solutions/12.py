n = int(input())
a = []
for i in range(n):
    a.append(input().split())
for i in range(int(n / 2)):
    a[i], a[n - i - 1] = a[n - i - 1], a[i]

for i in range(n):
    ln = len(a[i]) / 2
    for j in range(int(ln)):
        a[i][j], a[i][len(a[i]) - j - 1] = a[i][len(a[i]) - j - 1], a[i][j]
for i in range(n):
    for j in range(len(a[i])):
        for k in a[i][j]:
            if(not((k >= "a" and k <= "z") or (k >= "A" and k <= "Z") or (k >= "0" and k <= "9"))):
                a[i][j] = a[i][j][:len(a[i][j]) - 1]
for i in range(n):
    for j in range(len(a[i])):
        if(j == len(a[i]) - 1):
            print(a[i][j])
        else:
            print(a[i][j], end=" ")
