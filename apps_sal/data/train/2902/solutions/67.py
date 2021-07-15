def opposite(number):
    if number==abs(number):#If 1==1 then we should return negative number of the given digit
        return -abs(number)#Here we put up negative sign infront of abs() func
    else:
        return abs(number)#If number isn't equal to its absolute number then its negative, so return absolute number
