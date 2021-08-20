(num, loc) = map(int, input().split())
houses = list(map(int, input().split()))
ans = 10 ** 9
temp = []
for i in range(num):
    diff = abs(houses[i] - loc)
    if diff != 0:
        temp.append(diff)
temp.sort()
x = temp[0]
for i in range(len(temp)):
    if temp[i] % x == 0:
        continue
    else:
        x = 1
        break
print(x)
