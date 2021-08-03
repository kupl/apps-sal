for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    a = list(set(arr))
    for i in range(n):
        if i in a:
            arr[i] = i
            a.remove(i)
        else:
            arr[i] = 0

    print(*arr)
