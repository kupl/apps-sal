# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    candies = sum(a)
    ans = 0
    r = candies % n
    d = candies // n
    if(r == 0):
        ans = 0
    else:
        d = d + 1
        ans = (n * d) - candies
    for i in a:
        if(i > d):
            ans += i - d
    print(ans)
