t = int(input())
for you in range(t):
    n = int(input())
    s = input()
    curr = 0
    ans = 0
    for i in s:
        if i == '(':
            curr += 1
        else:
            curr -= 1
        if curr < 0:
            ans += 1
            curr = 0
    print(ans)
