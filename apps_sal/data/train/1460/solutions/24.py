(D, X, Y) = list(map(int, input().split()))
shifts = list(map(int, input().split()))
money = 0
for i in range(D):
    money = money + X + 0.8 ** (shifts[i] - 1) * Y
if money >= 300:
    print('YES')
else:
    print('NO')
