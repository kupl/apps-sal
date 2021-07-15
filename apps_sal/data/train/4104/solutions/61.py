def max_tri_sum(numbers):
    max = 0
    sum = 0
    i = 0
    result = []
    while i < 3:
        max = -9999999999
        for item in numbers:
            if item >= max:
                max = item
        
        if max not in result:
            result.append(max)
        
        for item in numbers:
            if item == max:
                numbers.remove(max)
        
        i += 1
        
    for item in result:
        sum += item

    return sum

