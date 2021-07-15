def is_triangle(a, b, c):
    listOfSides = [a,b,c]
    if max(listOfSides) >= (sum(listOfSides) - max(listOfSides)):
        return False
    return True
    
        

