def multiple_of_index(arr):
    answer = []
    for (i, a) in enumerate(arr):
        if i != 0 and a % i == 0:
            answer.append(a)
    return answer
