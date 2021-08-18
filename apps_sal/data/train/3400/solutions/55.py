def even_numbers(arr, n):

    result = []

    myList = arr
    evensList = [x for x in myList if x % 2 == 0]

    evensList = evensList[::-1]

    for i in range(0, n):

        result.append(evensList[i])

    return result[::-1]
