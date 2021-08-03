import heapq
n, q = list(map(int, input().split()))
event = []
for _ in range(n):
    s, t, x = list(map(int, input().split()))
    event.append((s - x, 1, x))
    event.append((t - x, -1, x))

event.sort()
heap = []
xs = set([])

d = [int(input()) for _ in range(q)] + [10**9 + 7]
ans = [-1] * q
index = 0
for t, query, x in event:
    while d[index] < t:
        if not xs:
            pass
        else:
            while heap:
                tmp = heapq.heappop(heap)
                if tmp in xs:
                    heapq.heappush(heap, tmp)
                    ans[index] = tmp
                    break
        index += 1

    if query == 1:
        xs.add(x)
        heapq.heappush(heap, x)
    else:
        xs.remove(x)


while index < q:
    while heap:
        tmp = heapq.heappop(heap)
        if tmp in xs:
            heapq.heappush(heap, tmp)
            ans[index] = tmp
            break
    index += 1

print(("\n".join(map(str, ans))))
