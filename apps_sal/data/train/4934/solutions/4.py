import heapq as hp


def sort(words):
    words = list(words)
    hp.heapify(words)
    while words:
        yield hp.heappop(words)
