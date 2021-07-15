import math
import heapq
def solve_workout(n_days, strength, plan, gain, costs):
    total_cost = 0
    heap = list()
    for i in range(n_days):
        heapq.heappush(heap, costs[i])
        n_doses = int(math.ceil((plan[i] - strength) / gain))
        while n_doses > 0 and heap:
            total_cost += heapq.heappop(heap)
            strength += gain
            n_doses -= 1
        if strength < plan[i]:
            return -1
    return total_cost
def __starting_point():
    N, K = tuple(map(int, input().split()))
    X = list(map(int, input().split()))
    A = int(input())
    C = list(map(int, input().split()))
    print(solve_workout(N, K, X, A, C))
__starting_point()
