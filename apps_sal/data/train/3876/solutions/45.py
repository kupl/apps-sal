def find(n):
    #Create a list's containing my multiples of 5 and 3
    a = list(range(5, (n)+1, 5))
    b = list(range(3, (n)+1, 3))
    
    # create sets of my list
    c = set(a)
    d = set(b)
    
    #remove the duplicates and create a list of removed duplicates
    e = list(d - c)
    
    #Sum list together
    return sum(a + e)
