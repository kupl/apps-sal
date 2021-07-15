def jumping_number(number):
    s = str(number)
    if len(s) == 1:
        return "Jumping!!"
    for i in range(len(s)-1):
        if(abs(int(s[i]) - int(s[i+1]))) != 1:
            return "Not!!"
            
    return "Jumping!!"
