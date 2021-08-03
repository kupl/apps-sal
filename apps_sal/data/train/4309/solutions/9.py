import itertools as it
from collections import Counter, defaultdict
from functools import reduce


def tokenize(string):
    groups = it.groupby(string)
    for key, group in groups:
        yield key, len(list(group))


def gather(tokens, expected_keys=None):
    stats = defaultdict(Counter)
    tokens = it.chain(tokens, ((key, 0) for key in expected_keys or []))
    for key, length in tokens:
        stats[key][length] += 1
    return stats


def intersect(*counters, ignored_keys=None):
    mins = reduce(lambda a, b: a & b, counters)
    for key in ignored_keys or []:
        mins.pop(key, None)
    return +mins


def remove(tokens, counters, replacement_key):
    for key, length in tokens:
        if counters[key][length]:
            counters[key][length] -= 1
            yield replacement_key, length
        else:
            yield key, length


def detokenize(tokens):
    return ''.join(key * length for key, length in tokens)


def replace(s):
    tokens = list(tokenize(s))
    stats = gather(tokens, expected_keys='!?')
    mins = intersect(*list(stats.values()), ignored_keys=[0])
    replace_counts = {key: mins.copy()for key in stats}
    replaced_tokens = remove(tokens, replace_counts, ' ')
    return detokenize(replaced_tokens)
