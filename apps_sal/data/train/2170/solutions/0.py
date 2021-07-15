import heapq

def sum_sqaure(a, k):
    q, r = divmod(a, k)
    return q**2 * (k-r) + (q+1)**2 * r

def diff(a, k):
    return sum_sqaure(a, k+1) - sum_sqaure(a, k)

n, k = map(int, input().split())
nums = list(map(int, input().split()))

curr = sum(sum_sqaure(a, 1) for a in nums)
Q = [(diff(a, 1), a, 1) for a in nums]
heapq.heapify(Q)
for __ in range(k - n):
    d, a, i = heapq.heappop(Q)
    curr += d
    heapq.heappush(Q, (diff(a, i+1), a, i+1))
print(curr)
