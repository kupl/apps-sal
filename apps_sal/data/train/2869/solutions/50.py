def distinct(seq):
    result_mas = []
    for i in seq:
        if i not in result_mas:
            result_mas.append(i)
    return result_mas
