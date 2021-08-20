test_case = int(input())
while test_case > 0:
    val = input()
    val = val.lower()
    if val == 'b':
        print('BattleShip')
    elif val == 'c':
        print('Cruiser')
    elif val == 'd':
        print('Destroyer')
    elif val == 'f':
        print('Frigate')
    test_case -= 1
