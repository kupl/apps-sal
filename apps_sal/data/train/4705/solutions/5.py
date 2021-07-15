def find_a_b(numbers,c):
    for i, x in enumerate(numbers): 
        for y in numbers[i+1:]: 
            if x*y == c: 
                return [x, y]
    return None
