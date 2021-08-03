def sum_of_minimums(numbers):
    pass
    print(('Input: ', numbers))
    x = 0
    mini = 0
    answer = []
    for i in numbers:
        mini = [min(numbers[x])]
        answer.append(mini)
        x += 1
    res = [sum(i) for i in zip(*answer)]
    stringres = [str(i) for i in res]
    finalres = int("".join(stringres))
    return int(finalres)
