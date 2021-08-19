def shortest_time(speed):
    copy = speed
    copy.sort()
    y = copy[0] + copy[1] * 3 + copy[3]
    minimum = copy.pop(0)
    answers = list()
    x = sum(copy) + minimum * (len(copy) - 1)
    answers.append(x)
    answers.append(y)
    return min(answers)
