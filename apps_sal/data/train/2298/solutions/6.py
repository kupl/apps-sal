import numpy as np
(N, T) = list(map(int, input().split()))
cost_list = np.array(list(map(int, input().split())))
max_num = 0
max_profit = 0
max_list = []
max_value = 0
for x in reversed(cost_list[1:]):
    max_value = max(max_value, x)
    max_list.append(max_value)
max_list = list(reversed(max_list))
max_list = np.array(max_list)
res = max_list - cost_list[:-1]
res_max = max(res)
max_num_list = [y for y in res if y == res_max]
print(len(max_num_list))
