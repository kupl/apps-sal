n = int(input())
l = list(map(int, input().split()))
for i in range(int(input())):
    c = 0
    quer = int(input())
    for i in range(n):
        for j in range(i + 1, n + 1):
            if min(l[i:j]) == quer:
                c += 1
    print(c)
