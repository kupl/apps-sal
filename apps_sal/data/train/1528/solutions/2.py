for _ in range(int(input())):
    (n, k) = map(int, input().split())
    arr = input().split()
    while arr and k:
        if arr.pop() == 'H':
            for i in range(len(arr)):
                if arr[i] == 'H':
                    arr[i] = 'T'
                else:
                    arr[i] = 'H'
        k -= 1
    res = sum((i == 'H' for i in arr))
    print(res)
