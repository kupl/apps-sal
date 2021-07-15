
def power_of_two(x):
  
    if x == 0:
        return False
    elif x & x-1 != 0:
        return False
    else:
        return True
    
    """
    count = 0
    while (x): 
        count += x & 1
        x >>= 1
    if count==1:
        return True
    else:
        return False
   
    string = bin(x)[2:]
    Sum=0
    for x in range(len(string)):
        if string[x]=="1":
            Sum+=1
    if Sum==1:
         return True
    else:
          return False
    """

