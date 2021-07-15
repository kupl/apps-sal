def even_numbers(arr,n):
    return [x for x in arr if not x%2][::-1][:n][::-1]
