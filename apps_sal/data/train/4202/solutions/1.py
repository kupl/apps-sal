import collections


def ulam_sequence(u0, u1, n):
    possible_sums = {}

    sequence = [u0, u1]

    for _ in range(0, n - 2):
        for term in sequence[:-1]:
            if term + sequence[-1] in possible_sums.keys():
                possible_sums[term + sequence[-1]] += 1
            else:
                possible_sums[term + sequence[-1]] = 1
        possible_sums = collections.OrderedDict(sorted(possible_sums.items()))
        next_term = min([sum for sum in possible_sums.keys() if possible_sums[sum] == 1 and sum not in sequence])
        sequence.append(next_term)

    return sequence
