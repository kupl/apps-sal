import math
test = int(input())
for _ in range(test):
    n = int(input())
    arr = [int(i) for i in input().split()]
    if len(arr) < 2:
        print(str(arr[0]) + ' ' + str(1))
        continue
    num1 = arr[0]
    num2 = arr[1]
    gcd = math.gcd(num1, num2)
    for i in range(2, len(arr)):
        gcd = math.gcd(gcd, arr[i])
    cost = 0
    for i in range(len(arr)):
        cost += arr[i] / gcd
    print(str(gcd) + ' ' + str(int(cost)))
