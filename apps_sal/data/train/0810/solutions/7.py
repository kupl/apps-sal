for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(q):
        s = list(map(int, input().split()))
        if s[0] == 0:
            arr[s[1]] = s[2]
        else:
            k = s[1]
            num = arr[k]
            if k == n - 1:
                print(-1)
                continue
            for j in range(k + 1, n):
                if arr[j] > num and arr[j] not in arr[:k]:
                    print(arr[j])
                    break
            else:
                print(-1)
