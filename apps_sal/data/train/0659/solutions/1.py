try:
    (n, k, s) = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    start = 0
    end = 0
    temp = 0
    for i in range(n):
        temp += arr[i]
        if temp > s and i - start + 1 > k:
            end = i
        while temp - arr[start] > s and end - start > k:
            temp -= arr[start]
            start += 1
    if end == start:
        print(-1)
    else:
        print(end - start + 1)
except:
    pass
