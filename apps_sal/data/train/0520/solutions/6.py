t=int(input())
for i in range(0,t):
    ch=input()
    if ch=='b' or ch=='B':
    	print("BattleShip\n")
    elif ch=='c' or ch=='C':
        print("Cruiser\n")
    elif ch=='D' or ch=='d':
        print("Destroyer\n")
    elif ch=='F' or ch=='f':
        print("Frigate\n")
