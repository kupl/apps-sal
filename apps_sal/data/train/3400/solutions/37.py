def even_numbers(array, number):
    a = []
    index = len(array) - 1
    while len(a) < number:
        if array[index] % 2 == 0:
            a.append(array[index])
        index -= 1
    return a[::-1]
