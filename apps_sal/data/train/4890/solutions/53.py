def find_difference(a, b):
    mul_a, mul_b = 1, 1
    
    for num_a, num_b in zip(a, b):
        mul_a *= num_a
        mul_b *= num_b
        
    return abs(mul_a - mul_b)
