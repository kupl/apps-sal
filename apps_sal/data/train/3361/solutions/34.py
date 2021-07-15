def sum_of_minimums(numbers):
    new_list = [ ]
    mini = 0
    for i in numbers:
        mini = min(i)
        new_list.append(mini)
    return sum(new_list)
