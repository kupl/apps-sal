def main():
    t = int(input())
    while t:
        n = int(input())
        lst = []
        for i in range(0, n):
            temp = input()
            temp = temp.split()
            lst.append(temp)
        print('Begin on', end=' ')
        l = len(lst)
        for i in range(0, len(lst[l - 1]) - 3):
            print(lst[l - 1][i + 2], end=' ')
        print(lst[l - 1][len(lst[l - 1]) - 1])
        for i in range(1, l):
            ind = l - i - 1
            if lst[ind + 1][0] == 'Left':
                print('Right on', end=' ')
            else:
                print('Left on', end=' ')
            for j in range(0, len(lst[ind]) - 3):
                print(lst[ind][j + 2], end=' ')
            print(lst[ind][len(lst[ind]) - 1])
        t = t - 1


def __starting_point():
    main()


__starting_point()
