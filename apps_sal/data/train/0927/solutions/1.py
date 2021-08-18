
n, m = tuple(map(int, input().split()))
if(n > 2):
    arr = [1, n]
elif(n == 1):
    arr = [1]
elif(n == 2):
    arr = [1, 2]

for i in range(m):
    k = int(input())
    if(n == 1):
        if(k != arr[0]):
            arr[0] = k
        print(arr[0])
    elif(n == 2):
        if(k == arr[0] or k == arr[1]):
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        else:
            arr[1] = k

        print(arr[0] + arr[1])

    else:
        ans = int(n * (n + 1) / 2) - 1 - n
        if(k == arr[0] or k == arr[1]):
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        elif(k > 1 and k < n):
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        else:
            arr[1] = k
        ans += arr[0] + arr[1]
        print(ans)
