t = int(input())
for _ in range(t):
    (s, n) = map(int, input().split())
    cnt = 0
    curr = n
    while s > 0 and curr != 0:
        cnt += s // curr
        s = s % curr
        curr = s // 2 * 2
    if s > 0:
        cnt += 1
    print(cnt)
