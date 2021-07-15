t = int(input())

for _ in range(t):
    n, k1, k2 = map(int, input().split())
    p1, p2, p3, p4 = map(int, input().split())
    sum = 0
    cont = [[[0, 0], -1] for _ in range(n)]
    for i in range(1, n+1):
        con = [x for x in range(1, n+1) if x%i == 0]
        
        for ele in con:
            if cont[ele-1][1] == -1:
                cont[ele-1][1] = 0
                cont[ele-1][0][0] += 1
                
            elif cont[ele-1][1] == 0:
                cont[ele-1][0][1] += 1
                cont[ele-1][1] = 1
            
            elif cont[ele-1][1] ==  1:
                if cont[ele-1][0] == [1, 1]:
                    cont[ele-1][1] = 3
                else:
                    cont[ele-1][1] = 0
                cont[ele-1][0][0] += 1
            
            elif cont[ele-1][1] == 3:
                cont[ele-1][0][1] += 1
                cont[ele-1][1] = 1
    
    for ele in cont[k1-1:k2]:
        # print(ele[1])
        if ele[1] == 0:
            sum += p2
        elif ele[1] == 2:
            sum += p4
        elif ele[1] == 3:
            sum += p1
        elif ele[1] == 1:
            sum+= p3
    print(sum)
