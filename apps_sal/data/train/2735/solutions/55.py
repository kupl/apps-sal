def jumping_number(number):
    n=str(number)
    if len(n)==1: return 'Jumping!!'
    else:
        x=0
        
        for x in range(0,len(n)-1):
            if abs(int(n[x])-int(n[x+1]))!=1:return 'Not!!'
            x+=1
    return 'Jumping!!'
