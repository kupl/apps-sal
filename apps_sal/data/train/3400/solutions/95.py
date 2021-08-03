def even_numbers(arr, n):
    even_steven = []
    for element in arr[::-1]:
        if element % 2 == 0 and len(even_steven) < n:
            even_steven.append(element)
    return even_steven[::-1]
