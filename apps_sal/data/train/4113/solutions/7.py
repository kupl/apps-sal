def solution(number):
    count = 0
    lst = []
    for i in range(1, number):
        if i % 3 == 0 and (not i % 5 == 0):
            count += 1
    lst.append(count)
    count = 0
    for i in range(1, number):
        if not i % 3 == 0 and i % 5 == 0:
            count += 1
    lst.append(count)
    count = 0
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            count += 1
    lst.append(count)
    return lst
