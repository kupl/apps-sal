def jumping_number(number):
    for i in range(len(str(number))-1) :
        if abs(int(str(number)[i+1])-int(str(number)[i]))!=1 : break
    else : return "Jumping!!"
    return "Not!!"

