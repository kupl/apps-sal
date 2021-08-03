points = [0, 40, 100, 300, 1200]


def get_score(arr) -> int:
    cleared = 0
    score = 0
    for lines in arr:
        level = cleared // 10
        score += (level + 1) * points[lines]
        cleared += lines
    return score
