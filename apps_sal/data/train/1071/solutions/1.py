for _ in range(int(input())):
    N,X=list(map(int,input().split()))
    string=[]
    while N//2!=0:
        string.append(N%2)
        N=N//2
    string.append(1)
    for _ in range(X):
        p=int(input())
        if p==1:
            i=int(input())
            if i-1<len(string):
                if (string[i-1]==1):
                    print("ON")
                    continue
                else:
                    print("OFF")
                    continue
            else:
                print("OFF")
                continue
        elif p==2:
            i =int(input())
            if i > len(string):
                x=i-len(string)
                for _ in range(x):
                    string.append(0)
                string[len(string)-1]=1
                continue
            else:
                string[i-1]=1
                continue
        elif p==3:
            i =int(input())
            if i > len(string):
                x=i-len(string)
                for _ in range(x):
                    string.append(0)
                continue
            else:
                string[i-1]=0
                continue
        else:
            j,k=list(map(int,input().split()))
            if j>len(string) or k >len(string):
                x=max(j,k)-len(string)
                for _ in range(x):
                    string.append(0)
                string[j-1],string[k-1]=string[k-1],string[j-1]
                continue
            else:
                string[j-1],string[k-1]=string[k-1],string[j-1]
                
        
                  
                
            
        

