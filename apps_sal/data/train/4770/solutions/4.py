from collections import defaultdict


def peak_height(mountain):
    heights = defaultdict(int)
    h, w = len(mountain), len(mountain[0])
    heights.update({(x, y): 0 if mountain[y][x] == " " else -1 for x in range(w) for y in range(h)})

    res = 0
    while True:
        todo = []

        for y in range(len(mountain)):
            for x in range(len(mountain[y])):
                if heights[(x, y)] == -1:
                    neighbors = [heights[(x + a, y + b)] for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)] if heights[(x + a, y + b)] > -1]

                    if neighbors:
                        todo.append((x, y, 1 + min(neighbors)))

        for x, y, v in todo:
            heights[(x, y)] = v
            res = max(res, v)

        if not todo:
            return res
