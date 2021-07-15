def jumping_number(number):
    n=str(number)
    if len(n)==1:
        return 'Jumping!!'
    else:
        for i in range(1,len(n)):
            if abs(int(n[i])-int(n[i-1]))==1:
                continue
            else:
                return 'Not!!'
        return "Jumping!!"
