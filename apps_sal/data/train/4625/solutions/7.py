def processes(start, end, processes):
    pss = []
    def proc(start, end, ps, l=[]): [pss.append(l + [ps[i][0]]) if ps[i][-1] == end else proc(ps[i][-1], end, ps[:i] + ps[i + 1:], l + [ps[i][0]]) for i in range(len(ps)) if ps[i][1] == start]
    return proc(start, end, processes) or (min(pss, key=len) if pss else [])
