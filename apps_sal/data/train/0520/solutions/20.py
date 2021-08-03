dec = {"b": "BattleShip", "c": "Cruiser", "d": "Destroyer", "f": "Frigate"}
for _ in range(int(input())):
    word = input().lower()
    print(dec[word])
