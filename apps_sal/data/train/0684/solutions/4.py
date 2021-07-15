try:
    import math
    # from collection import Counter
    def findAll(n):
        p = 0
        temp = []
        while n % 2 == 0: 
            p += 1  
            n = n / 2
        for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i== 0: 
                if i == 2:
                    p += 1
                else:
                    temp.append(i) 
                n = n / i 
        if n > 2: 
            temp.append(n)
        
        if p == 1:
            if len(temp) != 1:
                return True
            else:
                return False
        else:
            if len(temp) >= 1:
                return True
            else:
                return False
    t = int(input())
    while(t!=0):
        n = int(input())
        if n%2 != 0 and n != 1:
            print("Me")
        elif n%2 != 0 and n== 1:
            print("Grinch")
        elif n== 2:
            print("Me")
        else:
            if findAll(n) == True:
                print("Me")
            else:
                print("Grinch")

except EOFError:
    print(" ")
# This code is contributed by chandan_jnu 

