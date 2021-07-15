def divide(weight):
    if weight%2 == 0 or weight/10==int :
        a = weight/2 
        b = weight/2
        if a-1 == 0:
            return False
        elif a%2 == 0 and b%2 == 0:
            return True
        elif (a-1)%2 == 0 and (b+1)%2 == 0:
            return True
    else:
        return False
