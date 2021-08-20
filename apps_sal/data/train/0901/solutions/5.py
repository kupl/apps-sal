t = int(input())
while t > 0:
    t -= 1
    (n, k, s) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    temp = sorted(list(range(n)), key=lambda x: arr[x])
    arr.sort()
    ind = n - 1
    while ind > 1 and n >= 3:
        if arr[ind] > s:
            ind -= 1
        elif arr[ind] + arr[ind - 2] <= s:
            (arr[ind - 1], arr[ind]) = (arr[ind], arr[ind - 1])
            (temp[ind - 1], temp[ind]) = (temp[ind], temp[ind - 1])
            ind -= 2
        else:
            ind -= 1
    ans = [str(i + 1) for i in temp]
    print(' '.join(ans))
