number = int(input())
for i in range(number):
    x = list(map(int, input().split(' ')))
    print(x[0]%x[1])
