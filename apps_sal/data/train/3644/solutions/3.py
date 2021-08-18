import heapq


def add_all(arr):
    n = len(arr)
    heapq.heapify(arr)

    res = 0

    while(len(arr) > 1):

        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        res += first + second
        heapq.heappush(arr, first + second)

    return res
