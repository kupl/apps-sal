# cook your dish here
t = int(input())
ret = []
while t > 0:
    t -= 1
    n = int(input())
    s = input()
    arr = list(map(int, input().split(' ')))
    l = []
    f = True
    for i in range(len(arr)):
        if s[i] == '1':
            if f:
                fr = i
                f = False
            l.append(i)

    r = []
    for i in range(1, len(l)):
        r.append([l[i - 1], l[i]])

    # i = fr+1
    ans = 0
    for a in r:
        x = a[0]
        i = x + 1
        y = a[1]
        curr = arr[i] - arr[x]
        while i <= y:
            if arr[i] - arr[i - 1] > curr:
                curr = arr[i] - arr[i - 1]
            i += 1
        ans += abs(arr[y] - arr[x])
        ans -= curr
    ans += arr[fr] - arr[0]
    ans += arr[len(arr) - 1] - arr[l[len(l) - 1]]

    ret.append(ans)
for i in ret:
    print(i)
