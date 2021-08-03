def sum_of_minimums(numbers):
    mins = []
    for lists in numbers:
        lists.sort()
        mins.append(lists[0])
    return sum(mins)
