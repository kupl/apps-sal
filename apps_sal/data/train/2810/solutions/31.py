from string import ascii_lowercase
from collections import Counter

# try using zip


def solve(arr):

    counts = []

    for word in arr:

        count = Counter()

        zipped = list(zip(list(word.lower()), list(ascii_lowercase)))
        matches = [z for z in zipped if z[0] == z[1]]
        counts.append(len(matches))

    return counts
