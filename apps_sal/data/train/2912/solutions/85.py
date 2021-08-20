def find_multiples(integer, limit):
    li = []
    for i in range(0, limit + 1, integer):
        li.append(i)
    li.pop(0)
    return li
