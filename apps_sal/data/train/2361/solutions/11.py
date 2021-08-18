import heapq


def solve(n):
    h = [(-n, 0, n - 1)]
    sol = [0] * n
    curr = 1
    while h:
        _, l, r = heapq.heappop(h)
        mid = l + (r - l) // 2
        if l <= mid - 1:
            heapq.heappush(h, (l - mid + 1, l, mid - 1))
        if r >= mid + 1:
            heapq.heappush(h, (mid + 1 - r, mid + 1, r))
        sol[mid] = curr
        curr += 1
    return sol


t = int(input())
for _ in range(t):
    n = int(input())
    print(' '.join(map(str, solve(n))))
