def func(arr, k):
    sumi = 0
    for j in range(k):
        sumi += arr[j]
    maxi = sumi
    for i in range(k, len(arr)):
        sumi -= arr[i - k]
        sumi += arr[i]
        maxi = max(maxi, sumi)
    return maxi


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    arr = [int(x) for x in input().split()]
    print(func(arr, k))
