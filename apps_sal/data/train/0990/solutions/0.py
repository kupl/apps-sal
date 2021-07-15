try:
    n,m,a=map(int,input().split())
    if n%a!=0:
        number1=(n//a)+1
    else:
        number1=(n//a)
    if m%a!=0:
        number2=(m//a)+1
    else:
        number2=(m//a)
    print(number1*number2)
except:
    pass
