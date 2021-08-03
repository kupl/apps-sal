from heapq import heapify, heappush, heappop

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    l = list(map(int, input().split()))
    time = (n + 1) // 2

    h = []

    heapify(h)

    energy = max(l[0], l[-1])
    heappush(h, energy)

    for i in range(1, time):
        left, right = i, n - 1 - i

        mx = max(l[left], l[right])
        mn = min(l[left], l[right])

        energy += mx
        heappush(h, mx)

        if(left != right):
            if(h[0] < mn):
                energy -= h[0]
                heappop(h)
                energy += mn
                heappush(h, mn)

    if(energy >= x):
        print("YES")
    else:
        print("NO")
