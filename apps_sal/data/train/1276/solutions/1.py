t = eval(input())
x = [2**i for i in range(0, 20)]
for _ in range(t):
    n, k = list(map(int, input().split()))
    arr = set(map(int, input().split()))
    count = 0
    for i in x:
        if i in arr:
            count += 1
    if k - count <= 0:
        print(0)
    else:
        print(k - count)
