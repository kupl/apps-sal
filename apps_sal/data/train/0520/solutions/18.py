d = {'b': "BattleShip", 'B': "BattleShip", 'c': "Cruiser", 'C': "Cruiser", 'd': "Destroyer", "D": "Destroyer", 'f': "Frigate", 'F': "Frigate"}
t = int(input())
for i in range(t):
    a = input()
    print(d[a])
