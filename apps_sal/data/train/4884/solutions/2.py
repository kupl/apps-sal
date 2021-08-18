def connect_the_dots(paper):
    dots = {c: (i, j) for i, row in enumerate(paper.split("\n")) for j, c in enumerate(row) if c != " "}
    points = sorted(dots.keys())
    coords = sum((link(dots[a], dots[b]) for a, b in zip(points, points[1:])), list(dots.values()))
    return "\n".join("".join("*" if (i, j) in coords else " " for j, _ in enumerate(row)) for i, row in enumerate(paper.split("\n")))


def link(a, b):
    dx, dy = (-1 if a[i] > b[i] else 1 if a[i] < b[i] else 0 for i in (0, 1))
    return [(a[0] + dx * i, a[1] + dy * i) for i in range(1, abs(a[0] - b[0]) or abs(a[1] - b[1]))]
