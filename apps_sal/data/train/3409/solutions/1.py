from collections import Counter


def fish(shoal):
    (size, eaten) = (1, 0)
    for (fishesSize, n) in sorted(Counter(map(int, shoal)).items()):
        eaten += fishesSize * n if fishesSize <= size else 0
        size = 1 + int(((1 + 2 * eaten) ** 0.5 - 1) / 2)
    return size
