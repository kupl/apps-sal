t = int(input())
for asdf in range(t):
    n = int(input())
    dic = {}
    for sdfd in range(n):
        inp = input()
        split = inp.split(" ")
        if not split[0] in dic: 
            if int(split[1])==1:
                dic[split[0]] = [0, 1]
            else:
                dic[split[0]] = [1, 0]
        else:
            if int(split[1])==1:
                dic[split[0]][1] += 1
            else:
                dic[split[0]][0] += 1
    
    total = 0
    for x in dic:
        if dic[x][0]>= dic[x][1]:
            total += dic[x][0]
        else:
            total += dic[x][1]
    print(total)
