def billboard(name, price=30):
    #your code here - note that in Python we cannot prevent the use of the
    #multiplication, but try not to be lame and solve the kata in another way!
    tot = 0
    for x in name:
        tot += price
        
    return tot
