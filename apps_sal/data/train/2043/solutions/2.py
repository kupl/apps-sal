n = int(input())
ll = [list(map(int, input().split())) for _ in range(n)]
ll = [[0, 0]] + ll
tail = 0
visited = [False] * (n + 1)
cnt = 0
while cnt < n:
    for i in range(1, n + 1):
        if ll[i][0] == 0 and not visited[i]:
            head = i
            visited[head] = True
            cnt += 1
            break
    ll[tail][1] = head
    ll[head][0] = tail
    while ll[head][1] != 0:
        head = ll[head][1]
        visited[head] = True
        cnt += 1
    tail = head
for i in range(1, n + 1):
    print(ll[i][0], ll[i][1])
