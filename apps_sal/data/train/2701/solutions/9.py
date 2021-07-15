from math import floor

def get_score(arr) -> int:
    level = 1
    score = []
    counter = 0
    points = {0:0, 1:40, 2:100, 3:300, 4:1200}
    for i in arr:
        score.append(points[i]*level)
        counter += i
        level = floor(counter/10) + 1
    return sum(score)
