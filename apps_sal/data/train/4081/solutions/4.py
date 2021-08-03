def first_tooth(array):

    if len(array) <= 1:
        return 0

    differentials = []
    differentials.append(array[0] - array[1])

    for i in range(1, len(array) - 1):
        differentials.append(2 * array[i] - array[i - 1] - array[i + 1])

    differentials.append(array[-1] - array[-2])

    if differentials.count(max(differentials)) > 1:
        return -1
    else:
        return differentials.index(max(differentials))
