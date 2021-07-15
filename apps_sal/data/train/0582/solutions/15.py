
for _ in range(int(input())):
    s = input()
    n = int(input())
    l = list(map(int, input().split()))
    
    count = 0    
    stk = []
    last = -1
    store = [0] * len(s)
    
    
        
    for i in range(len(s)-1, -1, -1):
        if s[i] == ')':
            stk.append(i+1)
            if last == -1:
                store[i] = -1
            else:
                store[i] = last
                
        else:
            if len(stk) == 0:
                store[i] = -1
                last = -1
            else:
                x = stk.pop()
                store[i] = x
                last = x
                
    # print(store)
            
    for i in range(len(l)):
        print(store[l[i]-1])
        
        
        
        
        
            
            

