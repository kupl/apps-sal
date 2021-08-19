for test_case in range(int(input())):
    n = int(input())
    canvas = list(map(int, input().split(' ')))
    threes = 0
    if n > 2:
        for i in range(n - 2):
            if canvas[i] == canvas[i + 1] and canvas[i + 1] == canvas[i + 2]:
                threes += 1
    if threes > 0:
        print('Yes')
    else:
        print('No')
