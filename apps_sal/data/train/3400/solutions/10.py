def even_numbers(arr,n):
    return list(filter(lambda n: not n & 1, arr))[-n:]
