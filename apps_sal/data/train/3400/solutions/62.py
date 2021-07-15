def even_numbers(arr,n):
    li = [x for x in arr if x%2==0]
    li = li[::-1]
    result = li[:n]
    return result[::-1]

