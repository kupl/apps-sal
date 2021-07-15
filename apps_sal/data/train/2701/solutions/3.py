def get_score(arr) -> int:
    points = [0, 40, 100, 300, 1200]
    done = 0
    score = 0
    for lines in arr:
        level = done // 10
        score += (level+1) * points[lines]
        done += lines
    return score
