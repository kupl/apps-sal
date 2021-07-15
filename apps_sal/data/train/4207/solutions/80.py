def sum_cubes(n):

# There must be a shorter way!

    step1 = list(range(n))
    step2 = [x + 1 for x in step1]
        
    return sum([x**3 for x in step2])
        
    
    

