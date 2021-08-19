for _ in range(int(input())):
    (N, M) = map(int, input().split())
    arr = list(map(int, input().split()))
    arr1 = sorted(arr, reverse=True)
    lst = []
    for i in range(N):
        for j in range(i, N):
            x = arr[i:j + 1]
            x.sort(reverse=True)
            x.extend([0] * (N - len(x)))
            lst.append(x)
    lst.sort(reverse=True)
    for j in range(M):
        p = int(input()) - 1
        if p == N * (N + 1) // 2:
            print(min(arr))
        else:
            print(lst[p][0])
