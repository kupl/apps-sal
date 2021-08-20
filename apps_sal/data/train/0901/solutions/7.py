import random
t = int(input())
while t > 0:
    t -= 1
    (n, k, s) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    temp = sorted(list(range(n)), key=lambda x: arr[x])
    arr.sort()
    for j in range(5):
        for i in range(n - 1):
            if arr[i] + arr[i + 1] > s:
                (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
                (temp[i], temp[i + 1]) = (temp[i + 1], temp[i])
    ans = [str(i + 1) for i in temp]
    print(' '.join(ans))
