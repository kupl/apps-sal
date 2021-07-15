def my_first_kata(a,b):
    print('>>>'+str(a)+'<<< >>>'+str(b)+'<<<')
    if isinstance(a,bool) or isinstance(b,bool):
        return False
    if isinstance(a,int) and isinstance(b,int):
        return a % b + b % a if a!=0 and b!=0 else False
    return False
