points = [0, 40, 100, 300, 1200]


def get_score(arr):
    done, score = 0, 0
    for lines in arr:
        score += (done // 10 + 1) * points[lines]
        done += lines
    return score
