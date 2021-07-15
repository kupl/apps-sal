def array_madness(a,b):
   #descobrir o quadrado de cada elemento de a
    for i in range(len(a)):
        a[i] = a[i] ** 2 #levantado a 2 
    sum_a = sum(a)    
    
    for i in range(len(b)):
        b[i] = b[i] ** 3 #levantar 3
    sum_b = sum(b)
    
    if sum_a > sum_b:
        return True
    else:
        return False
        

