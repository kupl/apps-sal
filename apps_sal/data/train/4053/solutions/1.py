def reverse_factorial(num):
    n = 1
    f = 1
    while f < num:
        n += 1
        f = f * n
    return f"{n}!" if f == num else "None"
    
        

