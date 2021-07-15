def pattern(n) : 
    s=2*n-1
    for i in range(0, (s//2)+1):  
        m = n  
        for j in range(0, i):  
            print(m ,end= " " ) 
            m-=1
        for k in range(0, s - 2 * i): 
            print(n-i ,end= " " ) 
        m = n - i + 1
        for l in range(0, i):  
            print(m ,end= " " )  
            m+=1
        print("")  
    for i in range(s//2-1,-1,-1):  
        m = n  
        for j in range(0, i): 
            print(m ,end= " " ) 
            m-=1
        for k in range(0, s - 2 * i): 
            print(n-i ,end= " " ) 
        m = n - i + 1
        for l in range(0, i):  
            print(m ,end= " " )  
            m+=1
        print("")  
def __starting_point(): 
    n = int(input())
    pattern(n)  
__starting_point()
