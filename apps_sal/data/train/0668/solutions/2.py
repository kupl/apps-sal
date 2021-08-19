# cook your dish here
x = int(input())
for i in range(x):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ar = [i for i in arr] * k
    l = [0 for i in range(n * k)]
    l[0] = ar[0]
    for i in range(n * k):
        l[i] = max([l[i - 1] + ar[i], ar[i]])
    print(max(l))
