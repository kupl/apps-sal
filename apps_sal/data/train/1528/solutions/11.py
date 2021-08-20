for _ in range(int(input())):
    (N, k) = map(int, input().split())
    arr = list(map(str, input().split()))
    for i in range(1, k + 1):
        x = arr[len(arr) - i]
        arr[len(arr) - i] = '0'
        if x == 'H':
            for i in range(len(arr)):
                if arr[i] == 'H':
                    arr[i] = 'T'
                elif arr[i] == 'T':
                    arr[i] = 'H'
    print(arr.count('H'))
