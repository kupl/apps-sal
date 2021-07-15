def stringy(size):
    men =""
    for i in range(size):
        i +=1
        if i % 2 ==0:
            men+= "0"
        else:
            men += "1"
    return men
