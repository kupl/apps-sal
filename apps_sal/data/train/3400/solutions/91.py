def even_numbers(arr,n):
    new = [c for c in arr if c % 2 == 0]
    return new[-n:]
