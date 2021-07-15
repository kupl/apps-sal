def difference_in_ages(ages):
    goal = []
    goal.append(min(ages))
    goal.append(max(ages))
    goal.append(goal[1] - goal[0])
    return tuple(i for i in goal)
