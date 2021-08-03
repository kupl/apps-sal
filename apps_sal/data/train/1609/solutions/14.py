def sum_of_intervals(intervals):
    answer = []
    for tup in intervals:
        for j in range(tup[0], tup[1]):
            answer.append(j)
    return len(list(set(answer)))
