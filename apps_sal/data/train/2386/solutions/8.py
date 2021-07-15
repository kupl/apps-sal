t = int(input()) 
for _ in range (t): 

    n = int(input()) 
    seen = [False]*n 
    A = list(map(int, input().split())) 
    ans = list() 

    for a in A: 
        if not seen[a-1]: 
            seen[a-1] = True
            ans.append (a) 
    
    for a in ans: 
        print (a, end=" ") 
    print() 
