from collections import defaultdict


def __starting_point():
    (n, T) = [int(_) for _ in input().split()]
    data = defaultdict(list)
    for i in range(n):
        (t, q) = [int(_) for _ in input().split()]
        data[T - t].append(q)
    prev_level = []
    for level_id in range(1, T + 1):
        level = sorted(data[T - level_id] + prev_level, reverse=True)
        if T - level_id <= 10:
            max_size = 2 ** (T - level_id)
            level = level[:max_size]
        if len(level) % 2 == 1:
            level.append(0)
        prev_level = [level[i] + level[i + 1] for i in range(0, len(level), 2)]
    print(prev_level[0])


__starting_point()
