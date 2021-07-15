def jumping_number(number):
    print(number)
    a=[int(x) for x in list(str(number))]
    print(a) 
    if len(a)<2:
        return 'Jumping!!'
    return'Jumping!!' if all( a[i]==a[i+1]-1 or a[i]==a[i+1]+1 for i in range(len(a)-1 ))else'Not!!'
