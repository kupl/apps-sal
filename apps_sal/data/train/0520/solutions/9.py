t = int(input())
for i in range(t):
    id = input()
    if id == 'B' or id == 'b':
        print('BattleShip')
    if id == 'C' or id == 'c':
        print('Cruiser')
    if id == 'D' or id == 'd':
        print('Destroyer')
    if id == 'F' or id == 'f':
        print('Frigate')
