t = int(input())
for i in range(t):
    x = input()
    if x == 'B' or x == 'b':
        print('BattleShip')
    elif x == 'C' or x == 'c':
        print('Cruiser')
    elif x == 'D' or x == 'd':
        print('Destroyer')
    elif x == 'F' or x == 'f':
        print('Frigate')
