# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        if (i + k) % 7 == 0:
            c += 1
    print(c)
