def validate_rhythm(meter, score):
    print(score)
    if meter[1] not in [1, 2, 4, 8]:
        return "Invalid rhythm"
    goal = meter[0] * (1 / meter[1])
    print(goal)
    score = [[1 / int(f) for f in i] for i in score.split("|")]

    if len(score) == 1:
        if goal == sum([sum(i) for i in score]):
            return 'Valid rhythm'
        else:
            return 'Invalid rhythm'
    for i in score[1:-1]:
        if sum(i) != goal:
            return "Invalid rhythm"
    if sum(score[0]) + sum(score[-1]) == goal:
        return 'Valid rhythm with anacrusis'
    if sum(score[0]) + sum(score[-1]) != goal * 2:
        return "Invalid rhythm"
    return "Valid rhythm"
