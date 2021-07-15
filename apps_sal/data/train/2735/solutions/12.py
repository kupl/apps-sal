def jumping_number(number):
    string_n = str(number)
    l = len(string_n)
    if l <= 1: return "Jumping!!"
    else:
        for i in range(l-1):
            if abs(int(string_n[i]) - int(string_n[i+1])) != 1: return "Not!!"
    return "Jumping!!"
