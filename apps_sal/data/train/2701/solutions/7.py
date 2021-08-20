points = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}


def get_score(arr) -> int:
    sum = 0
    level = 0
    for i in arr:
        sum += points[i] * (int(level / 10) + 1)
        level += i
    return sum
