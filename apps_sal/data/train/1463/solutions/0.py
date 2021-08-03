def ugcd(n):
    ans = [[1]]
    if(n == 1):
        return ans
    elif(n % 2 == 1):
        ans = [[1, 2, n]]
    else:
        ans = [[1, 2]]
    for k in range(1, int(n // 2)):
        ans.append([k * 2 + 1, k * 2 + 2])
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    s = (ugcd(n))
    print(len(s))
    for j in range(len(s)):
        print(len(s[j]), end=" ")
        print(*s[j])
