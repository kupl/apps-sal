def count_sheep(n):
    x = " sheep..."
    z = ""
    for i in range(n): 
        y = str(i+1) + x
        z = z + y
    return z
