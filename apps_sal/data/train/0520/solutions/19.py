t = int(input())
for i in range(t):
    n = input()
    if n == 'B' or n == 'b':
        print('BattleShip')
    elif n == 'C' or n == 'c':
        print('Cruiser')
    elif n == 'D' or n == 'd':
        print('Destroyer')
    else:
        print('Frigate')
