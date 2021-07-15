def array_madness(a,b):
    a_sum = 0
    b_sum = 0
    for i in a:
        a_sum = a_sum + i**2
    for j in b:
        b_sum = b_sum + j**3
    
    if (a_sum > b_sum):
        return True
    else:
        return False
