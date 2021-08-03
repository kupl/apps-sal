import heapq


def sort(words):
    heap = []
    cnt = 0
    for w in words:
        cnt += 1
        heapq.heappush(heap, w)

    def sorted_gen():
        for i in range(cnt):
            yield heapq.heappop(heap)
    return sorted_gen()
