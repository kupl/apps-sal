import math


def isp(n):
    i = 2
    j = math.sqrt(n)
    while i <= j:
        if n % i == 0:
            break
        i += 1
    return i > j


t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    lst = [0] * 1000001
    ans = 1
    k = 0
    for x in arr:
        if(isp(x)):
            if lst[x] == 0:
                lst[x] = 1
                ans *= x
            else:
                k += 1
                break
        else:
            i = 2
            j = math.sqrt(x)
            while i <= j:
                if x % i == 0:
                    if lst[i] == 0 or lst[x // i] == 0:
                        break
                i += 1
            if i <= j:
                k += 1
                break
            else:
                if lst[x] == 0:
                    lst[x] = 1
                    ans *= x // math.gcd(ans, x)
                else:
                    k += 1
                    break

    if k:
        print(-1)
    else:
        if ans == arr[n - 1]:
            p = ans
            while p % arr[0] == 0:
                p //= arr[0]
            if p == 1:
                ans *= arr[0]
                print(ans)
            else:
                print(-1)
        else:
            print(ans)
    t -= 1
