def __starting_point():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ns = {}
        for _ in range(n - 1):
            _, *p = list(map(int, input().split()))
            tp = tuple(p)
            for pp in p:
                ns.setdefault(pp, set()).add(tp)
        first = [(k, list(v)[0]) for k, v in list(ns.items()) if len(v) == 1]
        found = False
        while not found:
            nns = {k: v.copy() for k, v in list(ns.items())}
            min_index = {}
            cur, cur_tp = first.pop()
            result = [cur]
            failed = False
            while len(nns) > 0 and not failed:
                nxt = set()
                for k in cur_tp:
                    mi = n - len(result) - len(cur_tp) + 1
                    min_index[k] = max(min_index.get(k, 0), mi)
                    nsk = nns[k]
                    nsk.remove(cur_tp)
                    if k == cur:
                        nns.pop(k)
                    elif len(nsk) == 1:
                        nxt.add(k)
                if len(nns) == len(nxt) or len(nns) == 1:
                    break
                if len(nxt) == 0:
                    failed = True
                else:
                    mmi = -1
                    for nx in nxt:
                        if min_index[nx] > mmi:
                            mmi = min_index[nx]
                            cur = nx
                    cur_tp = list(nns[cur])[0]
                    result.append(cur)
            if not failed:
                found = True
                if len(nns) == 1:
                    result.append(nns.popitem()[0])
                else:
                    a1, a2 = list(nns.keys())
                    if min_index[a1] == 1:
                        result.extend((a1, a2))
                    else:
                        result.extend((a2, a1))
                print(" ".join(map(str, reversed(result))))

__starting_point()
