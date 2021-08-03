# cook your dish here
n = int(input())
for i in range(n):
    x = input()
    if x == "b" or x == "B":
        print("BattleShip")
    elif x == "c" or x == "C":
        print("Cruiser")
    elif x == "d" or x == "D":
        print("Destroyer")
    else:
        print("Frigate")
