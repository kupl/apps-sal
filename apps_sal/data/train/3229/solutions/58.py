def fact(num):
   if num == 0:
       return 1
   return num * fact(num-1)
    
def am_i_wilson(n):
    print(n)
    if n <= 1:
        wp = 1    
    elif n > 999:
        wp=1
    else:
        #print(fact(n-1))
        wp = ((fact(n-1) + 1) % (n*n))
    return True if wp == 0 else False
    

