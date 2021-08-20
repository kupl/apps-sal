from itertools import combinations


def strings_crossover(arr, result):
    r = 0
    for (s1, s2) in combinations(arr, 2):
        flag = True
        for i in range(len(result)):
            if s1[i] != result[i] and s2[i] != result[i]:
                flag = False
                break
        if flag:
            r += 1
    return r
