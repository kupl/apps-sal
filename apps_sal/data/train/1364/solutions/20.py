# cook your dish here
for _ in range(int(input())):
    N, c = [int(i) for i in input().split()]
    coordinates, temp, checkpoints, operations = [], [], 0, 0
    for i in range(N):
        x, y = [int(i) for i in input().split()]
        temp.append(x)
        temp.append(y)
        coordinates.append(temp)
        temp = []
    dict1 = {}
    for i in coordinates:
        try:
            dict1[i[0] - i[1]].append(i[0])
        except:
            dict1[i[0] - i[1]] = [i[0]]
    # print(dict1)

    for i in dict1:
        list1 = dict1[i]
        list1.sort()
        dict2 = {}
        for j in list1:
            try:
                dict2[j % c].append(j)
            except:
                dict2[j % c] = [j]
        checkpoints += len(dict2)
        for k in dict2:
            list2 = dict2[k]
            median = list2[(len(list2) - 1) // 2]
            for ele in list2:
                operations += int(abs(median - ele) // c)
    print(checkpoints, operations)
