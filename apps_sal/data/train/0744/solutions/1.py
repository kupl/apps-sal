# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print("*")
    else:
        ii=0
        jj=0
        for i in range((n//2)+1):
            for j in range(i+1):
                if j==ii or j==jj:
                    print("*",end='')
                else:
                    print(" ",end='')
            print()
            jj+=1
        jj-=2
        for i in range((n//2),0,-1):
            for j in range(i+1):
                if j==ii or j==jj:
                    print("*",end='')
                else:
                    print(" ",end='')
            print()
            jj-=1
                
                
            
