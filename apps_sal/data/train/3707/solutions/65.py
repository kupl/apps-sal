def sorter(textbooks):
    arr = []
    for (i, book) in enumerate(textbooks):
        arr.append([book.lower(), i])
    arr = sorted(arr)
    for (i, book) in enumerate(arr):
        arr[i] = textbooks[book[1]]
    return arr
