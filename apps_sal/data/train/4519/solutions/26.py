from itertools import permutations


def max_number(n):
    answer = []
    max_combo = max(list(permutations([int(i) for i in str(n)])))
    for x in max_combo:
        if x not in answer:
            answer.append(str(x))
    return int(''.join(answer))
