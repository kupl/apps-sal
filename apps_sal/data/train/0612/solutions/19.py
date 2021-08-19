n = int(input())
for i in range(n):
    s = input()
    if '010' in s or '101' in s:
        print('Good')
    else:
        print('Bad')
