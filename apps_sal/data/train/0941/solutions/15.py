def esum(a, b):
    count = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i % 2 == 0 and j % 2 == 0:
                count += 1
            elif i % 2 != 0 and j % 2 != 0:
                count += 1
    return count


for i in range(int(input())):
    (x, y) = map(int, input().split(' '))
    print(esum(x, y))
