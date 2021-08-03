# cook your dish here
# cook your dish here
test = input()
for i in range(int(test)):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if i in arr:
            ans.append(i)
        else:
            ans.append(0)
    print(*ans)
