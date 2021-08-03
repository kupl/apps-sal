import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x)for x in input().split()]
    arr = list(dict.fromkeys(arr))
    arr.sort(reverse=True)
    if(len(arr) == 1):
        ans = 2 * arr[0]
        print(ans)
        continue
    n = len(arr)
    b = arr[0]
    c = arr[1]
    if(n >= 3):
        temp = arr[2]
        for i in range(2, n):
            temp = math.gcd(temp, arr[i])
        bval = math.gcd(b, temp)
        cval = math.gcd(c, temp)
        ans = max(bval + c, b + cval)
    else:
        ans = b + c
    print(ans)
