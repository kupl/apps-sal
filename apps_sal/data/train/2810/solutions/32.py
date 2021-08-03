from string import ascii_lowercase


def solve(arr):

    counts = []

    for word in arr:

        count = 0

        for idx, val in enumerate(word.lower()):

            if idx == ascii_lowercase.index(val):
                count += 1

        counts.append(count)

    return counts
