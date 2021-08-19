from itertools import permutations, chain
from math import factorial


def num_visible(row):
    visible = 0
    max_height = 0
    for i in row:
        if i > max_height:
            visible = visible + 1
            max_height = i
    return visible


def check_solution(solution, clues):
    solution = list(solution)
    solution = list(chain.from_iterable(solution))
    front_facing_key = {0: [0, 4, 8, 12], 1: [1, 5, 9, 13], 2: [2, 6, 10, 14], 3: [3, 7, 11, 15], 4: [3, 2, 1, 0], 5: [7, 6, 5, 4], 6: [11, 10, 9, 8], 7: [15, 14, 13, 12], 8: [15, 11, 7, 3], 9: [14, 10, 6, 2], 10: [13, 9, 5, 1], 11: [12, 8, 4, 0], 12: [12, 13, 14, 15], 13: [8, 9, 10, 11], 14: [4, 5, 6, 7], 15: [0, 1, 2, 3]}
    front_facing_values = {0: [0, 0, 0, 0], 1: [0, 0, 0, 0], 2: [0, 0, 0, 0], 3: [0, 0, 0, 0], 4: [0, 0, 0, 0], 5: [0, 0, 0, 0], 6: [0, 0, 0, 0], 7: [0, 0, 0, 0], 8: [0, 0, 0, 0], 9: [0, 0, 0, 0], 10: [0, 0, 0, 0], 11: [0, 0, 0, 0], 12: [0, 0, 0, 0], 13: [0, 0, 0, 0], 14: [0, 0, 0, 0], 15: [0, 0, 0, 0]}
    f_len = len(front_facing_values)
    for i in range(f_len):
        for j in range(4):
            front_facing_values[i][j] = solution[front_facing_key[i][j]]
    for i in range(f_len):
        if num_visible(front_facing_values[i]) != clues[i] and clues[i] != 0:
            return False
    return True


def solve_puzzle(clues):
    counter = 1
    for i in list(permutations([1, 2, 3, 4])):
        for j in list(permutations([1, 2, 3, 4])):
            for k in list(permutations([1, 2, 3, 4])):
                for l in list(permutations([1, 2, 3, 4])):
                    solution = (i, j, k, l)
                    trip = False
                    for m in range(4):
                        test = [i[m], j[m], k[m], l[m]]
                        if len(set(test)) != 4:
                            trip = True
                    if trip == False:
                        if check_solution(solution, clues):
                            return solution
    return 'No Solution'
