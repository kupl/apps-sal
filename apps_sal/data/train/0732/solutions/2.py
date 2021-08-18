for _ in range(int(input())):
    n = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if arr1[i] == arr2[i] and sum(arr1[:i]) == sum(arr2[:i]):
            res += arr1[i]
    print(res)
