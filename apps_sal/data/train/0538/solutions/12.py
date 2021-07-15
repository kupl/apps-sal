for _ in range(int(input())):
    S,SG,FG,D,T=map(int, input().strip().split())
    G=S+((180*D)/T)
    if abs(G-SG)>abs(G-FG):
        print("FATHER")
    elif abs(G-SG)<abs(G-FG):
        print("SEBI") 
    else:
        print("DRAW")
