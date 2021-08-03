def symmetric_point(p, q): return[q[i] + abs(p[i] - q[i])if p[i] < q[i]else q[i] - abs(p[i] - q[i])if p[i] > q[i]else q[i] for i in (0, 1)]
