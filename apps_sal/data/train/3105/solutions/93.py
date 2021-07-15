def count_sheep(n):
    
    #set up empty string
    x = ""
    
    #for all i in range 0-n, add a sheep comment to x
    # number is i+1 as index starts from zero
    for i in range(n):
        x = x+(str(i+1)+" sheep...")
       
    # now return the full string
    return x
