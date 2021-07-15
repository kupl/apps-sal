# cook your dish here
t=int(input())
for i in range(t):
    n=input()
    if(n=='b' or n=='B'):
        print('BattleShip')
    elif(n=='c' or n=='C'):
        print('Cruiser')
    elif(n=='d' or n=='D'):
        print('Destroyer')
    else:
        print('Frigate')
