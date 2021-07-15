def balanced_num(number):
    if number<100:
        return 'Balanced'
    else:
        a1,a2=0,0
        if len(str(number))%2==0:
            for i in range(0,len(str(number))//2-1):
                a1+=int(str(number)[i])
                a2+=int(str(number)[len(str(number))-i-1])
        else:
            for i in range(0,len(str(number))//2+1):
                a1+=int(str(number)[i])
                a2+=int(str(number)[len(str(number))-i-1])
        if a1==a2:
            return 'Balanced'
        else:
            return 'Not Balanced'

