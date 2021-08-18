w = int(input())


def checkEqual(lst):
    return lst[1:] == lst[:-1]


v = 0
while v < w:
    sign = 0
    v += 1
    [n, d] = [int(i) for i in input().split()]
    arr = list(map(int, input().split()))
    my_dict = {}
    i = 0
    while i < d:
        my_dict[i] = list()
        j = 0
        while i + j < n:
            my_dict[i].append(arr[i + j])
            j += d
        i += 1
    mean = float(sum(arr)) / len(arr)
    if mean % 1 != 0.0:
        print(-1)
        continue
    else:
        means = []
        for i in range(d):
            means.append((sum(my_dict[i]) / len(my_dict[i])))
        if not(checkEqual(means)):
            print(-1)
            continue
        steps = 0
        for x in range(d):
            for y in range(len(my_dict[x])):
                if (my_dict[x][y] < mean):
                    steps += mean - my_dict[x][y]
                    my_dict[x][y + 1] -= mean - my_dict[x][y]
                    my_dict[x][y] = mean
                elif (my_dict[x][y] > mean):
                    steps += my_dict[x][y] - mean
                    my_dict[x][y + 1] += my_dict[x][y] - mean
                    my_dict[x][y] = mean
                elif (my_dict[x][y] == mean):
                    continue
                else:
                    print('impossible')
        print(int(steps))
