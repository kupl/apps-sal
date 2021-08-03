def even_numbers(arr, n):

    a = [i for i in arr if i % 2 == 0]

    return a[-n::]
