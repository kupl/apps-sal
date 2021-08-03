
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if i in a:
            a[i] = i
        else:
            a[i] = 0
    print(*a)
# cook your dish here
