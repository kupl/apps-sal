def shallowest_path(river):
    depth = {(r, c): d for r, row in enumerate(river) for c, d in enumerate(row)}
    width = max(c for _, c in depth)

    for mx in sorted(set(depth.values())):
        D = {d for d in depth if depth[d] <= mx}
        paths, D = [[d] for d in D if d[1] == 0], {d for d in D if d[1]}

        while paths:
            newp = []
            for p in paths:
                if p[-1][1] == width:
                    return p
                for d in {(p[-1][0] + rr, p[-1][1] + cc) for rr in [-1, 0, 1] for cc in [-1, 0, 1]} & D:
                    newp, _ = newp + [p + [d]], D.discard(d)
            paths = newp
