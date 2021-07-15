def jumping_number(n):
    for i in range(len(str(n))-1):
        if abs(int(str(n)[i])-int(str(n)[i+1])) != 1:
            return "Not!!"
    return "Jumping!!"
