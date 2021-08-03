def distinct(seq):
    answer = []
    for a in seq:
        if answer.count(a) == 0:
            answer.append(a)
    return answer
