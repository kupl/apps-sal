t = int(input())
i = 0
while i < t:
    n = input()
    if n == 'b' or n == 'B':
        print('BattleShip')
    if n == 'c' or n == 'C':
        print('Cruiser')
    if n == 'd' or n == 'D':
        print('Destroyer')
    if n == 'f' or n == 'F':
        print('Frigate')
    i += 1
