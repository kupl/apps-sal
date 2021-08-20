def leaderboard_climb(arr, kara):
    scores = sorted(set(arr), reverse=True)
    position = len(scores)
    ranks = []
    for checkpoint in kara:
        while position >= 1 and checkpoint >= scores[position - 1]:
            position -= 1
        ranks.append(position + 1)
    return ranks
