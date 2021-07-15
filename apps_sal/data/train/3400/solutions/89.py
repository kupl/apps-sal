def even_numbers(arr,n):
    l = []
    counter = 1
    while len(l) != n:
        if arr[-counter] % 2 == 0:
            l.append(arr[-counter])
        counter +=1
    return l[::-1]
            
        

