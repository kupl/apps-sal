def jumping_number(number):
    t = str(number)
    i = 0
    if len(t) == 1:
        return "Jumping!!"
    
    while i < len(t)-1:
        if (int(t[i+1]) - int(t[i])) == 1 or (int(t[i+1]) - int(t[i])) == -1 :
            i = i + 1
        else: 
            return "Not!!"
    return "Jumping!!"
