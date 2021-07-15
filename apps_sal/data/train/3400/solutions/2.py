def even_numbers(arr,n):
    return list(filter(lambda n: n % 2 == 0, arr))[-n:]
