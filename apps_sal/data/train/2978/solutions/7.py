import collections

def count_sel(lst):
    counter = collections.Counter(lst)
    mode_count = counter.most_common(1)[0][1] if lst else 0
    return [len(lst),
            len(counter),
            sum(v == 1 for v in counter.values()),
            [sorted(k for k, v in counter.items() if v == mode_count), mode_count]]
