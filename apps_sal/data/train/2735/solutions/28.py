def jumping_number(number):
    numero = str(number)
    res = []
    if len(numero) == 1:
        return "Jumping!!"
    else:
        for i in range(len(numero)-1): 
            if (int(numero[i]) - int(numero[i + 1])) == 1 or (int(numero[i]) - int(numero[i + 1])) == -1:
                res.append(0)   
            else:
                res.append(1)
            
    if sum(res) == 0:
        return "Jumping!!"
    else:
        return "Not!!"
