def count_sheep(n):
    
    sheeps = ""
    
    for i in range(1,n+1):
        sheep = f"{i} sheep..."
        sheeps += sheep
        
    return sheeps
