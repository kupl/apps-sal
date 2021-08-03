# cook your dish here
x = int(input())
for i in range(x):
    y = input()
    y = y.lower()
    if(y == "b"):
        print("BattleShip")
    if(y == "c"):
        print("Cruiser")
    if(y == "d"):
        print("Destroyer")
    if(y == "f"):
        print("Frigate")
