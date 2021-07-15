def even_or_odd(number):
    string = ""
    
    #check last bit of number, if 1 number is odd, if 0 number is even
    if (number & (1>>0)):
        string = "Odd"
    else: 
        string = "Even"
    return string
