from bisect import bisect_left, bisect_right, insort

n = int(input())
s = list("-" + str(input()))
lis = [[] for i in range(26)]
for i in range(1, n + 1):
    num = ord(s[i]) - ord("a")
    lis[num].append(i)

q = int(input())
for turn in range(q):
    query = list(map(str, input().split()))
    if query[0] == "1":
        a = int(query[1])
        if s[a] == query[2]:
            continue
        num = ord(s[a]) - ord("a")
        lis[num].pop(bisect_left(lis[num], a))
        next = ord(query[2]) - ord("a")
        insort(lis[next], a)
        s[a] = query[2]
    else:
        a, b = int(query[1]), int(query[2])
        ans = 0
        for alphabet in range(26):
            if bisect_right(lis[alphabet], b) - bisect_left(lis[alphabet], a) >= 1:
                ans += 1
        print(ans)
