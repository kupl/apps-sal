a = []

for i in range(11):
    a.append(int(input()))
    
for i in range(10,-1,-1):     
   
    temp =(abs(a[i]))**(1/2) + 5*a[i]**3
    if temp >= 400:
        print("f({}) = MAGNA NIMIS!".format(a[i]) )
    else:
        print("f({}) = {:.2f}".format(a[i], temp) )
    

   

