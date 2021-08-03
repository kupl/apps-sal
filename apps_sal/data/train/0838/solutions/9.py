t = int(input())
while t:
    t -= 1
    n = int(input())
    L = [int(x) for x in input().split()]
    L.reverse()
    count = 0
    for i in range(n):
        if L[i] > count:
            count = L[i]
        count += 1
    print(count - 1)
