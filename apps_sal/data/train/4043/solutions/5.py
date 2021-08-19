def calc(gamemap):
    nr, nc = len(gamemap), len(gamemap[0])
    vs, ws = [0] * nr**2, [0] * nr**2
    vs[0] = gamemap[0][0]
    for s in range(nr + nc - 2):
        for ra in range(min(s + 1, nr)):
            ca = s - ra
            for rb in range(ra, min(s + 1, nr)):
                cb = s - rb
                v = vs[ra * nr + rb]
                for da in (0, 1):
                    ra_, ca_ = ra + da, ca + (1 - da)
                    if ra_ < nr and ca_ < nc:
                        for db in (0, 1):
                            rb_, cb_ = rb + db, cb + (1 - db)
                            if rb_ < nr and cb_ < nc:
                                v_ = v + gamemap[ra_][ca_] + (gamemap[rb_][cb_] if ra_ != rb_ else 0)
                                ws[ra_ * nr + rb_] = max(ws[ra_ * nr + rb_], v_)
        vs, ws = ws, vs
    return vs[-1]


# # Unoptimized:
# from collections import defaultdict, namedtuple

# def calc(gamemap):
#     nr, nc = len(gamemap), len(gamemap[0])
#     vs = {(Point(0, 0), Point(0, 0)): gamemap[0][0]}
#     for _ in range(nr + nc - 2):
#         ws = defaultdict(int)
#         for (a, b), v in vs.items():
#             for a_ in a.next_points(nr, nc):
#                 for b_ in b.next_points(nr, nc):
#                     v_ = v + gamemap[a_.r][a_.c] + (gamemap[b_.r][b_.c] if a_ != b_ else 0)
#                     ws[a_, b_] = max(ws[a_, b_], v_)
#         vs = ws
#     return vs[Point(nr-1, nc-1), Point(nr-1, nc-1)]

# class Point(namedtuple('Point', 'r c')):
#     def next_points(self, nr, nc):
#         if self.c < nc - 1:
#             yield Point(self.r, self.c + 1)
#         if self.r < nr - 1:
#             yield Point(self.r + 1, self.c)
