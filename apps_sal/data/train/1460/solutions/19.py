D, X, Y = map(int, input().split())
workingDays = list(map(int, input().split()))
listOfTips = [Y]
for i in range(1, 6):
    temp = listOfTips[0] - (0.02 * i * (listOfTips[0]))
    listOfTips.append(temp)

# print(listOfTips)
total = D * X
# print(total)
for i in workingDays:
    #print(i,"  ",listOfTips[i-1])
    total += listOfTips[i - 1]

# print(total)

print("YES") if total >= 300 else print("NO")
