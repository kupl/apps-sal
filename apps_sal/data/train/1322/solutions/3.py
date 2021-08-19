# cook your dish here
t = int(input())
for j in range(t):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    c = 0
    l.sort(reverse=True)
    for i in range(n):
        if l[i] >= l[k - 1]:
            c += 1
    print(c)
