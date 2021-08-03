def points(game_results):
    return sum(get_points(result) for result in game_results)


def get_points(result):
    left_score = int(result[0])
    right_score = int(result[-1])
    if left_score > right_score:
        return 3
    elif left_score < right_score:
        return 0
    elif left_score == right_score:
        return 1
