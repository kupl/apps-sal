n = int(input())
l = list(map(int, input().split()))
x = int(input())
count = 0
k = []
for i in range(n):
    if l[i] < 0:
        count += 1
        k.append(l[i])
y = count
k.sort()
z = y - x
k.reverse()
sum = 0
h = 0
for i in range(len(k)):
    k[i] += h
    if y > x:
        sum += abs(k[i] * x)
        h += abs(k[i])
    else:
        sum += abs(k[i] * y)
        h += abs(k[i])
    y -= 1
print(sum)
