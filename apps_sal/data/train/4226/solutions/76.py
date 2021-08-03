def remove_smallest(numbers):
    print(numbers)
    sort = sorted(numbers)
    if sort == []:
        return []
    else:
        min = sort[0]
    count = 0
    new = []

    for i in numbers:
        if i == min and count < 1:
            count += 1
            continue
        else:
            new.append(i)
    return new
