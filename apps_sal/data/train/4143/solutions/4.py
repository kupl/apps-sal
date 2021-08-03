def points(d): return ((c := list(map(d.count, '123456'))) in (5 * [1] + [0], [0] + 5 * [1], [1, 0] + 4 * [1])) * 20 + (3 in c) * (2 in c) * 30 + (4 in c) * 40 + (5 in c) * 50
