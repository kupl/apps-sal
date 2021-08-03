from collections import Counter


def runoff(voters):
    cands = [cand for cand in voters[0] if cand]
    first_col = [row[0] for row in voters]
    counter = Counter(first_col)

    for candidate in counter:
        if counter[candidate] > len(voters) / 2:
            return candidate and candidate or None

    excluded = [x for x in counter if counter[x] == min(counter.values())]
    excluded.extend(set(cands) - set(first_col))

    for arr in voters:
        for i, x in enumerate(arr):
            if x in excluded:
                arr[i] = None

    out = []
    for arr in voters:
        names, banned = [], []
        for val in arr:
            if val:
                names.append(val)
            else:
                banned.append(val)

        out.append(names + banned)

    return runoff(out)
