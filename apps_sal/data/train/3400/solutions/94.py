def even_numbers(arr,n):
    return list(reversed([x for x in arr if x%2==0][-1:-(n+1):-1]))
