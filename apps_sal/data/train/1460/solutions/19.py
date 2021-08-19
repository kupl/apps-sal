(D, X, Y) = map(int, input().split())
workingDays = list(map(int, input().split()))
listOfTips = [Y]
for i in range(1, 6):
    temp = listOfTips[0] - 0.02 * i * listOfTips[0]
    listOfTips.append(temp)
total = D * X
for i in workingDays:
    total += listOfTips[i - 1]
print('YES') if total >= 300 else print('NO')
