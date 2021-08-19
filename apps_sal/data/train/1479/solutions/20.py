# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(11):
        arr.append(0)
    for i in range(n):
        p, s = list(map(int, input().split()))
        if p <= 8:
            arr[p - 1] = max(arr[p - 1], s)
    print(sum(arr))
