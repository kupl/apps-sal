def even_numbers(arr, n):
    L = [i for i in arr if i % 2 == 0]
    return L[-n:]
