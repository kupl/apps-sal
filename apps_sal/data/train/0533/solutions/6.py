T = int(input())

for t in range(T):
    K,N = map(int,input().split())
    data = list(map(int,input().split()))
    
    first = -1
    
    for i in range(len(data)):
        if(data[i]==K):
            first = i
            break
            
    second = -1
    
    for i in range(len(data)-1,first,-1):
        if(data[i]==K):
            second = i
            break
            
    if(first == -1 or second == -1):
        print(0)
    else:
        print(second-first)
