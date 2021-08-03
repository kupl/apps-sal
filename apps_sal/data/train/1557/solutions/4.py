# cook your dish here
for i in range(int(input())):
    n = int(input())
    t = list(input())
    j = list(input())
    if t.count('1') == j.count('1'):
        print('YES')
    else:
        print('NO')
