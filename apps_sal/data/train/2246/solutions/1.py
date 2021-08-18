from heapq import *


def main():
    n, k = input().split()
    n = int(n)
    k = int(k)
    req = list(map(lambda x: int(x), input().split()))
    each = int(input())
    prices = list(map(lambda x: int(x), input().split()))
    total = 0
    hp = []
    heapify(hp)
    for i in range(n):
        heappush(hp, prices[i])
        needed = (req[i] - k + each - 1) // each
        needed = max(0, needed)
        if len(hp) < needed:
            print(-1)
            return
        for j in range(needed):
            total += heappop(hp)
            k += each
    print(total)


main()
