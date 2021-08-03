from collections import deque
import heapq

n = int(input())
cards_help = list(map(int, input().split()))
cards = [(cards_help[i], -1 * i) for i in range(n)]
heapq.heapify(cards)

draws = 0
removed = 0
while cards:
    prev = -1
    new_removals = 0
    current = cards[0]
    while cards and -1 * current[1] > prev:
        new_removals += 1
        heapq.heappop(cards)
        temp_prev = -1 * current[1]
        while cards and cards[0][0] == current[0] and -1 * cards[0][1] > prev:
            current = cards[0]
            heapq.heappop(cards)
            new_removals += 1
        prev = temp_prev
        current = cards[0] if cards else 0
    draws += n - removed
    removed += new_removals
print(draws)
