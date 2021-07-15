from sys import stdin, stdout 
for t in range(int(stdin.readline())):
    s = str(stdin.readline()) 
    q = int(stdin.readline())
    a =  list(map(int, stdin.readline().split()))
    d = {}
    stc = []
    p = -1
    for i in range((len(s) - 1), -1, -1):
        if(s[i] == ')'):
            stc.append(i)
            d[i+1] = p
        elif(s[i] == '('):
            if(len(stc) >= 1):
                d[i+1] = stc[-1] + 1
                p = d[i + 1]
                stc.pop()
            else:
                d[i+1] = -1
                p = d[i + 1]
                
    for i in a:
        print(d[i])
        
        
        

