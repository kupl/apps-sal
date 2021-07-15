def remove_duplicate_words(s):
    arr = s.split()
    arr1 = []
    for el in arr:
        if not el in arr1:
            arr1.append(el)
    return " ".join(arr1)

