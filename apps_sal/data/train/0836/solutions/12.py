t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    maxv = -1
    for i in range(n):
        a = l[i] * r[i]
        if a >= maxv:
            if a == maxv:
                if prevr < r[i]:
                    index = i
                    prevr = r[i]
            else:
                index = i
                prevr = r[i]
                maxv = a
    print(index + 1)
