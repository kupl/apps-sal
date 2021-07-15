t = int(input())
for _ in range(t):
    n = int(input())
    l = list(input())
    d = int(input())
    wall = list(map(str, input().split()))
    lst = l.copy()
    # 3 == 0 & 2 == 1
    god = []
    for i in range(n):
        if(l[i]=='1' or l[i] == '2'):
            god.append(i)
            
            
    for i in range(d):
        
        if(l[int(wall[i]) - 2] =='0'):
            l[int(wall[i]) - 2] = '3'
        else:
            l[int(wall[i]) - 2] = '2'
        lst = l.copy()    
        # print(l)
        god = list(set(god))
        bap = god.copy()
        
        # print("bap", bap)
        for j in bap:
            if(j==0 or j==n-1):
                continue
            # print(j, end = "   ")
            if(lst[j]=='1'):
                if(l[j-1] == '0'):
                    l[j-1] = '1'
                    god.append(j-1)
                if(l[j+1] == "0"):
                    l[j+1] = '1'
                    god.append(j+1)
                if(l[j+1] == "3"):
                    l[j+1] = '2'
                    god.append(j+1)
            elif(lst[j]=='2'):
                if(l[j-1] == '0'):
                    god.append(j-1)
                    l[j-1] = '1'
            # print("in loop", l)        
        if(lst[0]=='1'):
            if(l[1]=='0'):
                l[1] = '1'
                god.append(1)
            elif(l[1]=='3'):
                l[1] = '2'
        if(lst[n-1]=='1'):
            if(l[n-2]=='0'):
                l[n-2] = '1'
                god.append(n-2)
        # print("god", god)
        # print("check 0 and n-1", l)    
    # print(l)               
    print(l.count('1') + l.count('2'))            
        
            

