number = int(input())
sum = 0
array = input().split()
array2 = []
for i in array:
    array2.append(int(i))
array2.sort()
array2 = array2[::-1]
for i in range(0, number):
    sum = sum + int(array2[i])
games = int(sum / (number - 1))
if sum % (number - 1) > 0:
    games = games + 1
if games < array2[0]:
    games = array2[0]
print(games)
