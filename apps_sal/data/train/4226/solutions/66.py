def remove_smallest(numbers):
    count = 0
    a= []
    for x in numbers:
        if x == min(numbers) and count == 0:
            count +=1
            continue
        else :
            a.append(x)
    return a
        
        

