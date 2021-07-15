from collections import Counter

def solve(s):
    frequencies = [x[1] for x in Counter(s).most_common()]
    return (
        len(frequencies) == 1 or
        len(set(frequencies[:-1])) == 1 and frequencies[-1] == 1 or
        frequencies[0] == frequencies[1] + 1 and len(set(frequencies[1:])) == 1)
