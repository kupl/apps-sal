T = int(input())
for _ in range(T):
    string = input()
    if '101' in string or '010' in string:
        print('Good')
    else:
        print('Bad')
