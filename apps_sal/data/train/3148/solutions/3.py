def simplify(path):
    x, y, coords = 0, 0, [(0, 0)]
    for c in path:
        x += 1 if c == ">" else -1 if c == "<" else 0
        y += 1 if c == "^" else -1 if c == "v" else 0
        if (x, y) in coords:
            i = coords.index((x, y))
            path, coords = path[:i] + path[len(coords):], coords[:i]
        coords.append((x, y))
    return path

