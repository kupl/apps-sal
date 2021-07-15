J = int(input())

for i in range(J):
    N,data = int(input()),list(map(int,input().split()))
    if(N==3):
        print(sum(data))
    else:
        best = data[0]+data[1]+data[2]
        overall = best
        for i in range(1,len(data)-2):
            overall=overall - data[i-1] + data[i+2]
            if(overall>best):
                best = overall
        if(best < data[-1]+data[0]+max(data[1],data[-2])):
            best = data[-1] + data[0] + max(data[1],data[-2])
        print(best)
