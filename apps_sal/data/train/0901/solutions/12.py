import random
t = int(input())
while t > 0:
    t -= 1
    (n, k, s) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    temp = sorted(list(range(n)), key=lambda x: arr[x])
    '\n    arr = sorted(arr, reverse=True)\n    ind = 0\n    while arr[ind]>s:\n        ind += 1\n    temp = temp[ind:] + temp[:ind]\n    '
    ans = [str(i + 1) for i in temp]
    print(' '.join(ans))
