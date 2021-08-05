import sys
n = eval(input())
parents = [int(x) - 1 for x in input().split(' ')]
values = list(map(int, input().split(' ')))
parents = [0] + parents
# print(parents)
# print(values)


def single_node_cost(i):
    cost = 0
    # print('started with ',i)
    min_value = sys.maxsize
    while i != 0:
        min_value = min(min_value, values[i])
        cost += min_value
        # print(i,min_value)
        i = parents[i]
    cost += min(values[0], min_value)
    return cost


for i in range(n):
    print(single_node_cost(i), end=' ')
