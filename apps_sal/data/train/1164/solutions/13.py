from collections import *
(P, S) = input().split()
P = int(P)
S = int(S)
list_of_dictionaries = []
for _ in range(P):
    scores = input().split()
    number_of_contestants = input().split()
    scores = map(int, scores)
    number_of_contestants = map(int, number_of_contestants)
    dictionary = dict(zip(scores, number_of_contestants))
    dictionary = OrderedDict(sorted(dictionary.items()))
    list_of_dictionaries.append(dictionary)
list_of_difficulty_tuples = []
for alpha in range(P):
    current_dictionary = list_of_dictionaries[alpha]
    old = -1
    n = 0
    for v in current_dictionary.values():
        if old == -1:
            old = v
        elif v < old:
            n = n + 1
            old = v
        else:
            old = v
    list_of_difficulty_tuples.append((n, alpha + 1))
list_of_difficulty_tuples = sorted(list_of_difficulty_tuples)
for result in range(len(list_of_difficulty_tuples)):
    print(list_of_difficulty_tuples[result][1])
