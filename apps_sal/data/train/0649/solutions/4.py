def left(list1):
    for i in range(len(list1)):
        list2 = sorted(list1[i])
        list2.reverse()
        list1[i] = list2


def right(list1):
    for i in range(len(list1)):
        list2 = sorted(list1[i])
        list1[i] = list2


def up(list1):
    for i in range(len(list1[0])):
        list2 = []
        for j in range(len(list1)):
            list2.append(list1[j][i])
        list2.sort()
        list2.reverse()
        for j in range(len(list1)):
            list1[j][i] = list2[j]


def down(list1):
    for i in range(len(list1[0])):
        list2 = []
        for j in range(len(list1)):
            list2.append(list1[j][i])
        list2.sort()
        for j in range(len(list1)):
            list1[j][i] = list2[j]


test_case = int(input())
result = []
for i in range(test_case):
    [n, m] = list(map(int, input().split()))
    list1 = []
    for i in range(n):
        y = list(input())
        str2 = ' '.join(y)
        list1.append(list(map(int, str2.split())))
    op = list(input())
    for i in range(len(op)):
        if op[i] == 'L':
            left(list1)
        if op[i] == 'R':
            right(list1)
        if op[i] == 'D':
            down(list1)
        if op[i] == 'U':
            up(list1)
    result.append(list1)
for char in result:
    for el in char:
        print(''.join(list(map(str, el))))
