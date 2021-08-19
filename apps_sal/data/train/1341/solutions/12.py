# cook your dish here
import bisect

for t in range(int(input())):
    n = int(input())
    arr = [int(a) for a in input().split()]
    prifix = list()
    prefix = [False for _ in range(n)]
    for i in range(0, n):
        if(i == 0):
            prefix[i] = True
        else:
            if arr[i] > arr[i - 1]:
                prefix[i] = True
            else:
                break
    sufix = list()
    sufix = [False for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if(i == n - 1):
            sufix[i] = True
        else:
            if arr[i] < arr[i + 1]:
                sufix[i] = True
            else:
                break
    left = 0
    right = 0
    for i in range(n):
        if prefix[i] == True:
            left = i
    for i in range(n - 1, -1, -1):
        if sufix[i] == True:
            right = i
    ans = 0
    if right == 0 and left == n - 1:
        ans = (n * (n + 1) // 2) - 1

    else:
        i = 0
        while(prefix[i] == True):
            if arr[i] > arr[n - 1]:
                ans += 1
            else:
                k = bisect.bisect_left(arr, arr[i], right, n - 1)
                ans += n - k + 1
                if(arr[k] == arr[i]):
                    ans -= 1
            i += 1
        ans += n - right
    print(ans)
