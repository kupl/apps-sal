test_case = int(input())
while test_case > 0:
    angle = [int(x) for x in input().split(' ')]
    if sum(angle) == 180:
        print('YES')
    else:
        print('NO')
    test_case -= 1
