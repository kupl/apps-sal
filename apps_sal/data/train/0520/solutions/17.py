t = int(input())

for i in range(t):
    num = (input())
    if (num == "B" or num == "b"):
        print("BattleShip")
    elif (num == "C" or num == "c"):
        print("Cruiser")
    elif (num == "D" or num == "d"):
        print("Destroyer")
    elif (num == "F" or num == "f"):
        print("Frigate")
