a, b = list(map(int, input().split()))
l = []
for _ in range(a):
    x = int(input())
    l.append(x)

l.sort()

m = 0
i = 0
while(i < a - 1):
    x = l[i + 1] - l[i]
    if(x <= b):
        m = m + 1
        i = i + 2
    else:
        i = i + 1
print(m)
