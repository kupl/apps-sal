rooms = int(input())
money = list(map(int, input().split()))
keys = int(input())
rev = -1
a, b = 0, -1
tot = []
# print(money[-3:-1])
x = 0
for i in range(keys):
    # print(money[b:-1],money[0:a])
    x = sum(money[b:]) + sum(money[0:keys - abs(b)])
    tot.append(x)
    b -= 1
print(max(tot))
