def is_divisible(n,x,y):
    #your code here
    div1=n % x
    div2=n % y
    if div1 == 0 and div2 == 0:
       return True
    else:
       return False

print(is_divisible(6,2,3))
