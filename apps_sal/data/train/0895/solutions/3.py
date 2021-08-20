import math
N = int(input().strip())
costs = [int(i) for i in input().strip().split(' ')]
stored_val_1 = [costs[0], costs[0] + costs[1]]
stored_val_2 = [math.inf, costs[1]]
for (idx, cost) in enumerate(costs[2:]):
    stored_val_1.append(cost + min(stored_val_1[-1], stored_val_1[-2]))
for (idx, cost) in enumerate(costs[2:]):
    stored_val_2.append(cost + min(stored_val_2[-1], stored_val_2[-2]))
print(min(stored_val_1[-1], stored_val_1[-2], stored_val_2[-1]))
