t = int(input())
while t:
    t = t - 1
    n = input()
    if '101' in n or '010' in n:
        print('Good')
    else:
        print('Bad')
