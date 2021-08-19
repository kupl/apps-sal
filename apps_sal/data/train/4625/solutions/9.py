from collections import defaultdict


def prcs(start, end, procs, path):
    if start == end:
        return path
    paths = []
    try:
        for p in procs[start]:
            if p in path:
                continue
            paths.append(prcs(p[1], end, procs, path + [p]))
        return min([a for a in paths if a and a[-1][1] == end], key=len)
    except (KeyError, ValueError):
        return []


def processes(start, end, procs):
    dd = defaultdict(list)
    for (n, s, e) in procs:
        dd[s].append((n, e))
    return [n for (n, _) in prcs(start, end, dd, [])]
