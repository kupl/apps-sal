# cook your dish here
n=int(input())
for i in range(n):
    S, SG, FG, D, T = map(int, input().split())
    speed = (D*180)/T + S
    if abs(SG-speed) == abs(FG-speed):
        print('DRAW')
    elif abs(SG-speed) > abs(FG-speed):
        print('FATHER')
    else:
        print('SEBI')
