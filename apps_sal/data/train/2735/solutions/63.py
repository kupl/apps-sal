def jumping_number(number):
    if len(str(number))==1:
        return "Jumping!!"
    else:
        res = list(map(int,str(number)))
        for i in range(len(res)-1):
            if abs(res[i+1]-res[i])!=1:
                return "Not!!"
                break
        return "Jumping!!"
                

