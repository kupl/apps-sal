def even_numbers(arr,n):
    output = [i for i in arr if i % 2 == 0]
    return output[-n:]
