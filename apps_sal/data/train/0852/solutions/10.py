for i in range(int(input())):
    n= int(input())
    
    for j in range(0,n):
        s=""
        for k in range(1,n+1):
            if (j+k)%2==1:
                s+="0"
            else:
                s+="1"
        print(s)    

