import numpy as np


def sort_it(array):
    new_list = []
    for i in range(len(array)):
        start = 0
        value = array[i][0]
        last = len(new_list)
        while start != last:
            mid = (start + last) // 2
            if new_list[mid][0] > value:
                last = mid
            else:
                start = mid + 1
        new_list.insert(start, array[i])
    return new_list


tests = int(input())
for _ in range(tests):
    (n, m, q) = [int(j) for j in input().split()]
    challenges = [[0] * 3 for _ in range(m)]
    combos = [[0] * 2 for _ in range(q)]
    for i in range(m):
        challenges[i] = [int(j) for j in input().split()]
    for i in range(q):
        combos[i] = [int(j) for j in input().split()]
    sorted_chalenges = np.zeros((2 * m, 3), dtype=np.intc)
    for i in range(m):
        sorted_chalenges[2 * i] = [challenges[i][0] - 1, challenges[i][2], i]
        sorted_chalenges[2 * i + 1] = [challenges[i][1], -challenges[i][2], i]
    sorted_chalenges = np.array(sort_it(sorted_chalenges))
    types_of_players = np.zeros((m + 1, 2 * m + 1), dtype=np.intc)
    player_type = np.zeros(n, dtype=np.intc)
    last_player = 0
    for i in range(2 * m):
        (start, value, chal) = sorted_chalenges[i]
        types_of_players[chal + 1:, i + 1:] += value
        player_type[last_player:start] = i
        last_player = start
    player_type[last_player:] = 2 * m
    combo_types = np.zeros((q, 2 * m + 1), dtype=np.intc)
    for i in range(q):
        (first, last) = combos[i]
        (r, p) = [types_of_players[first - 1], types_of_players[last]]
        combo_types[i] = np.maximum(p - r, 0)
    output = np.sum(combo_types, axis=0)[player_type]
    for i in range(n):
        print(output[i], end=' ')
    print('')
