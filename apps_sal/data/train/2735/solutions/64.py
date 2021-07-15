def jumping_number(number):
    if number<10:
        return "Jumping!!"

    number=str(number)
    lnm=[]
    for i in number:
        lnm.append(i)
    for i in range(len(lnm)-1):
        if abs(int(lnm[i])-int(lnm[i+1]))!=1:
            return "Not!!"
    else:
        return "Jumping!!"
