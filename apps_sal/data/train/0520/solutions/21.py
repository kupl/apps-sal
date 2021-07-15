# cook your dish here
dec= {"B":"BattleShip","C":"Cruiser","D":"Destroyer","F":"Frigate","b":"BattleShip","c":"Cruiser","d":"Destroyer","f":"Frigate"}
T = int(input())
for i in range(T):
    word = input()
    print(dec[word])
