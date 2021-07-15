def even_numbers(arr, n):
    return list([e for e in arr if e % 2 == 0])[-n::]

