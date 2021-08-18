from itertools import permutations


def palindrome_pairs(words):
    result = []
    for i, j in permutations(list(range(len(words))), 2):
        concat = f"{words[i]}{words[j]}"
        if concat == concat[::-1]:
            result.append([i, j])
    return result
