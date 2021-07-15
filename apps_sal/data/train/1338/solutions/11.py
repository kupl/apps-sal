
List = [float(x) for x in input().split()]
x = 1
for i in range(int(List[0])):
    
    X = str(round(List[x]*(10**List[x+1]),2))
    if(X[-2]=="."):
        X+="0"
    print(X)
    x+=2
