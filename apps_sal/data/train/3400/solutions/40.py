def even_numbers(arr, n):
    print([a for a in arr if a % 2 == 0][-n:])
    return [a for a in arr if a % 2 == 0][-n:]
