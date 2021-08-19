d = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}


def get_score(arr) -> int:
    (level, score, line) = (0, 0, 0)
    for n in arr:
        score += d[n] * (level + 1)
        line += n
        level = line // 10
    return score
