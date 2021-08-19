t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    arr = list(map(str, input().split()))
    for i in range(k):
        if arr[-1] == 'H':
            for j in range(len(arr)):
                if arr[j] == 'H':
                    arr[j] = 'T'
                else:
                    arr[j] = 'H'
        g = arr.pop()
    print(arr.count('H'))
