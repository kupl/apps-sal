t = int(input())
while t > 0:
    t -= 1

    n, k, s = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    temp = sorted(list(range(n)), key=lambda x: arr[x])
    arr.sort()
    ind = n - 1
    while ind > 0:
        if arr[ind] > s:
            ind -= 1
        elif arr[ind] + arr[ind - 1] > s and arr[ind] + arr[0] <= s:
            temp = temp[ind:ind + 1] + temp[:ind] + temp[ind + 1:]
            break
        else:
            break
    ans = [str(i + 1) for i in temp]
    print(' '.join(ans))
