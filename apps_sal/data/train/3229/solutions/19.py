def am_i_wilson(n):
    print(n)
    if prime(n)==False: return False
    elif prime(n)==True:
        if n==5 or n==13 or n==563: return True
        else: return False

    
def prime(num):
    if num%2==0 or num==1: return False
    
    for i in range(1,int(num**0.5)+2):
        if num%i==0 and i!=1:
            return False
    return True


