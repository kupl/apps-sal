import heapq
from math import ceil
for _ in range(int(input())):
    (N, A, B, X, Y, Z) = map(int, input().split())
    C = list(map(int, input().split()))
    heap = [-contrib for contrib in C]
    heapq.heapify(heap)
    hooli_days = ceil((Z - B) / Y)
    piper_init_gap = Z - A
    if ceil((piper_init_gap - 2 * sum(C)) / X) >= hooli_days:
        print('RIP')
    else:
        num_contribs = 0
        while ceil(piper_init_gap / X) >= hooli_days and any(heap):
            contrib = -heapq.heappop(heap)
            piper_init_gap -= contrib
            heapq.heappush(heap, -(contrib >> 1))
            num_contribs += 1
        if ceil(piper_init_gap / X) < hooli_days:
            print(num_contribs)
        else:
            print('RIP')
