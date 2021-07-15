import heapq

def sort_number(a):
    l = a[:]
    heapq._heapify_max(l)
    mx = heapq.heappop(l)
    heapq.heappush(l, 2 if mx == 1 else 1)
    return heapq.nsmallest(len(a), l)
