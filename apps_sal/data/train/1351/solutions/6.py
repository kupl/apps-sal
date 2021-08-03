# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i in a:
            ans.append(i)
        else:
            ans.append(0)
    print(*ans)
