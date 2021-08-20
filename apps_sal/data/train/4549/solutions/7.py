import sys
sys.setrecursionlimit(15000)


def lemming_battle(battlefield, green, blue):
    (green, blue) = [p[::-1] for p in map(sorted, (green, blue))]
    k = min(battlefield, len(min(green, blue, key=len)))
    (g, b) = (green[:k], blue[:k])
    (a_green, a_blue) = ([], [])
    for (a, b) in zip(g, b):
        if abs(a) - abs(b):
            if a > b:
                a_green.append(a - b)
            else:
                a_blue.append(b - a)
    (green, blue) = (sorted(a_green + green[k:], reverse=True), sorted(a_blue + blue[k:], reverse=True))
    if not green + blue:
        return 'Green and Blue died'
    if not blue:
        return f"Green wins: {' '.join(map(str, sorted(green, reverse=1)))}"
    if not green:
        return f"Blue wins: {' '.join(map(str, sorted(blue, reverse=1)))}"
    else:
        return lemming_battle(battlefield, green, blue)
