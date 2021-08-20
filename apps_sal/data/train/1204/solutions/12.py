import heapq


def minops(s, r):
    letter = 0
    heap = []
    k = 0
    for i in range(len(s)):
        if s[i] != r[i]:
            letter += 1
            if i + 1 == len(s) or s[i + 1] == r[i + 1]:
                k += 1
                g = 0
        elif k != 0:
            g += 1
            if i + 1 != len(s) and s[i + 1] != r[i + 1]:
                heapq.heappush(heap, g)
    mini = k * letter
    while k > 0 and len(heap) > 0:
        k -= 1
        gap = heapq.heappop(heap)
        letter += gap
        if k * letter < mini:
            mini = k * letter
    return mini


t = int(input())
for _ in range(t):
    s = input()
    r = input()
    print(minops(s, r))
