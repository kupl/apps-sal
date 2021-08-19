n = int(input())
while n:
    n = n - 1
    s = input()
    li = s.split(' ')
    l = int(li[0])
    r = int(li[1])
    ans = r
    while r >= l:
        ans = r
        r = r & r + 1
        r = r - 1
    print(ans)
