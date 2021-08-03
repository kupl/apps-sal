
t = input()
p = input()
a = [i - 1 for i in list(map(int, input().split()))]
min1 = 0
max1 = len(t)
while(max1 - min1) > 1:
    med = min1 + (max1 - min1) // 2
    j = 0
    d = list(t)
    for i in range(med):
        d[a[i]] = ''
    for i in range(len(t)):
        if d[i] == p[j]:
            j += 1
            if j == len(p):
                min1 = med
                break
    if j != len(p):
        max1 = med
print(min1)
