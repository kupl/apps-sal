from itertools import groupby


def substring(strng):
    return max(
        enumerate(iter_candidates(strng, 2)),
        key=lambda ix: (len(ix[1]), -ix[0]),
    )[1]


def iter_candidates(strng, n):
    xs = []
    seen = set()
    for c, grp in groupby(strng):
        if len(seen) >= n and c not in seen:
            yield "".join(xs)
            seen.discard(xs[-n][0])
            del xs[:1 - n]
        xs.append("".join(grp))
        seen.add(c)
    yield "".join(xs)
