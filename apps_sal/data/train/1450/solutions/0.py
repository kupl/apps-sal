# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 1
    while(i < n):
        a[i - 1], a[i] = a[i], a[i - 1]
        i += 2
    print(*a)
