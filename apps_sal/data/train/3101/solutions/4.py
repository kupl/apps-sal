from itertools import permutations


def palindrome_pairs(words):
    result = []
    for i, j in permutations(list(range(len(words))), 2):
        concat = f"{words[i]}{words[j]}"
        if concat == concat[::-1]:
            result.append([i, j])
    return result


# one-liner
# def palindrome_pairs(w):
#    return [[i, j] for i, j in permutations(range(len(w)), 2) if f"{w[i]}{w[j]}" == f"{w[i]}{w[j]}"[::-1]]
