def best_match(goals1, goals2):
    num = goals1[0] - goals2[0]
    goal = 0
    for i in range(len(goals1)):
        if goals1[i] - goals2[i] < num:
            num = goals1[i] - goals2[i]
            goal = i
        if goals1[i] - goals2[i] == num:
            if goals2[i] > goals2[goal]:
                goal = i
    return goal
