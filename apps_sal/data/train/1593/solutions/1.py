n = int(input())
def count (x) :
    m = 0  
    if (x - 100 >= 0) :
        m = int(x/100)
        x = x%100 
    if (x - 50 >= 0):
        m = int(x/50) + m
        x = x%50
    if (x - 10 >= 0):
        m = int(x/10) + m 
        x = x%10
    if (x - 5 >= 0) :
        m = int(x/5) + m 
        x = x%5
    if (x - 2 >= 0) :
        m = int(x/2) + m 
        x= x%2
    if (x - 1 >= 0) :
        m = 1 + m 
    return (m)    
    
for i in range (n) :
    x = int(input())
    p = count(x)
    print(p)
    

