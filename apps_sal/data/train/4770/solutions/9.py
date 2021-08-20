def peak_height(mountain):

    def condition1(a, b, mountian):
        return a == 0 or a == len(mountain) - 1 or b == 0 or (b == len(mountain[0]) - 1)

    def condition2(a, b, k):
        if k == -1:
            return any([mountain_list[a + 1][b] == ' ', mountain_list[a - 1][b] == ' ', mountain_list[a][b + 1] == ' ', mountain_list[a][b - 1] == ' '])
        else:
            return any([mountain_list[a + 1][b] == k + 1, mountain_list[a - 1][b] == k + 1, mountain_list[a][b + 1] == k + 1, mountain_list[a][b - 1] == k + 1])

    def loop_firt(list):
        for (a, i) in enumerate(list):
            for (b, j) in enumerate(i):
                if j == '^' and condition1(a, b, mountain):
                    list[a][b] = 1
                elif j == '^' and condition2(a, b, -1):
                    list[a][b] = 1

    def loop_again(list, y):
        for (a, i) in enumerate(list):
            for (b, j) in enumerate(i):
                if j == '^' and condition1(a, b, mountain):
                    pass
                elif j == '^' and condition2(a, b, y - 1):
                    list[a][b] = y + 1

    def the_biggest(list):
        for i in mountain_list:
            for j in i:
                if type(j) == int:
                    yield j
                elif j == ' ':
                    pass
    if mountain == []:
        return []
    x = ['^', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    mountain_list = []
    list2 = []
    for i in mountain:
        list1 = []
        for j in i:
            list1.append(j)
        mountain_list.append(list1)
    for i in range(len(x)):
        if i == 0:
            loop_firt(mountain_list)
        else:
            loop_again(mountain_list, i)
    for i in mountain_list:
        list1 = []
        for j in i:
            list1.append(str(j))
        list2.append(''.join(list1))
    if list(the_biggest(mountain_list)) == []:
        return 0
    else:
        return max(list(the_biggest(mountain_list)))
