# cook your dish here
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    k = p = 0
    for i in range(n):
        if l[i] % 2 == 0:
            k += 1
        else:
            p += k
    print(p)
