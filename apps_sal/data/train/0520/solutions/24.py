for i in range(int(input())):
    ele = input()
    if(ele == 'B' or ele == 'b'):
        print('BattleShip')
    elif(ele == 'C' or ele == 'c'):
        print('Cruiser')
    elif(ele == 'D' or ele == 'd'):
        print('Destroyer')
    else:
        print('Frigate')
