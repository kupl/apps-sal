def men_from_boys(arr):
    return list(dict.fromkeys(sorted([num for num in arr if num % 2 == 0]) +
                              sorted([num for num in arr if num % 2 != 0], reverse=True)))
