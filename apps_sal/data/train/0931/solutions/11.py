# cook your dish here
try:
    t = int(input())
    
    while t:
        n = int(input())
        arr = [int(i) for i in input().split()]
        des = 0
        for elm in arr:
            try:
                if elm%2 == 0:
                    des += elm
            except:
                pass            
        print(des)
        t -= 1 
except:
    pass
