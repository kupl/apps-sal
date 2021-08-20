test = int(input())
for i in range(test):
    no_cars = int(input())
    L = [int(x) for x in input().split()]
    cars_fast = 1
    for j in range(no_cars - 1):
        if L[j] >= L[j + 1]:
            cars_fast = cars_fast + 1
        else:
            L[j + 1] = L[j]
    print(cars_fast)
