def multiple_of_index(arr):
    new = []
    x = 1
    for i in arr[1:]:
        if i % x == 0:
            new.append(i)
        x += 1
            
    return new
