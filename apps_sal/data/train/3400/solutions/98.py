def even_numbers(arr,n):
    cont = 0
    m = []
    x = -1
    
    while cont < n:
        if arr[x] % 2 == 0:
            m.append(arr[x])
            cont += 1
        x = x - 1
    m.reverse()
    return m

