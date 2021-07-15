def is_divisible(n,x,y):
    #number being divided
    #x , y numbers being used to divide
    #print false if its not divisible by one number
    #print true if both statements are true
    if n % x == 0 and n % y == 0:
        return True
    elif n % x != 0 or n % y != 0:
        return False
