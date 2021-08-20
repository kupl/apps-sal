from queue import PriorityQueue
(n, k) = map(int, input().split())
x = list(map(int, input().split()))
a = int(input())
c = list(map(int, input().split()))
tot = 0
pq = PriorityQueue()
for i in range(0, n):
    if k >= x[i]:
        pq.put(c[i])
    else:
        pq.put(c[i])
        while pq.qsize():
            ans = pq.get()
            k += a
            tot += ans
            if k >= x[i]:
                break
        if k < x[i]:
            tot = -1
            break
print(tot)
