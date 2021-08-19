# cook your dish here
T = int(input())
for i in range(T):
    n = input()
    if n == "B" or n == "b":
        print("BattleShip")
    if n == "C" or n == "c":
        print("Cruiser")
    if n == "D" or n == "d":
        print("Destroyer")
    if n == "F" or n == "f":
        print("Frigate")
