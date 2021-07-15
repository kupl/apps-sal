def even_numbers(arr,n):
    newarr = [i for i in arr if i%2 == 0]
    return newarr[-n:]
