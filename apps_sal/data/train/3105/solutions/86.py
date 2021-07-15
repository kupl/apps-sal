def count_sheep(n):
    total = ""
    x = 0
    for i in range(n):
        x += 1
        total += str(x)+" sheep..."
        
    return total
