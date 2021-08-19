def gcd(x, y):
    if not y:
        return x
    return gcd(y, x % y)


for t in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    s = False
    for i in range(len(arr) - 1):
        temp = gcd(arr[i], arr[i + 1])
        if temp == 1:
            print(len(arr))
            s = True
            break
        else:
            arr[i + 1] = temp
    if not s:
        print(-1)
