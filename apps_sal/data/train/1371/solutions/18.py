t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = [x + k for x in lst]
    c = 0
    for i in lst:
        if i % 7 == 0:
            c += 1
    print(c)
