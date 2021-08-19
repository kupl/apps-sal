def fun(li, k):
    head = [0] * len(li)
    tail = [0] * len(li)
    for i in range(1, len(li)):
        if li[i - 1] == '1':
            head[i] = head[i - 1] + 1
        else:
            head[i] = 0
    for i in range(len(li) - 2, -1, -1):
        if li[i + 1] == '1':
            tail[i] = tail[i + 1] + 1
        else:
            tail[i] = 0
    ans = 0
    for i in range(0, len(li) - k + 1):
        ans = max(ans, k + head[i] + tail[i + k - 1])
    return ans


t = int(input())
for i in range(0, t):
    s = list(map(int, input().strip().split()))
    s1 = s[0]
    s2 = s[1]
    li = input()
    print(fun(li, s2))
