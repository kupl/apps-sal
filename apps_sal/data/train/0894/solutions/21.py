import random
t = int(input())
for testCase in range(t):
    n = int(input())
    array1 = [0] * n
    array2 = [0] * n
    for i in range(2 * n):
        array = input()
    for i in range(n):
        array1[i] = array2[i] = i + 1
    for i in range(n):
        rand = random.randint(0, len(array1) - 1)
        print(array1[rand], end=' ')
        array1.pop(rand)
    print()
    for i in range(n):
        rand = random.randint(0, len(array2) - 1)
        print(array2[rand], end=' ')
        array2.pop(rand)
    print()
