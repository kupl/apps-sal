def jumping_number(number):
    string= str(number)
    for i in range(len(string)-1):
        if abs(int(string[i]) - int(string[i+1])) != 1: return "Not!!"
    return "Jumping!!"        

