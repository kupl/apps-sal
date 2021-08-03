import sys
tokenizedInput = sys.stdin.read().split()


def triplets(n, arr):
    array = sorted(arr, reverse=False)
    temp = []
    result = []
    i = 0
    for i in range(len(array)):
        if i < len(array) - 2:
            if array[i] + array[i + 1] > array[i + 2]:
                temp.append(array[i])
                temp.append(array[i + 1])
                temp.append(array[i + 2])
                i = 3
                temp = sorted(temp, reverse=False)
                for i, num in enumerate(temp):
                    if temp[0] + temp[1] > temp[2]:
                        result.append(sorted(temp, reverse=True))
                temp = []
            else:
                i += 1
    max = 0
    i = 0
    if result:
        for count, eacharr in enumerate(result):
            if eacharr[0] > max:
                max = eacharr[0]
                i = count
        listToStr = ' '.join([str(elem) for elem in result[i]])
        print('YES')
        print(listToStr)
    else:
        print('NO')


def main():
    lst = []

    n = list(map(int, tokenizedInput[:1]))
    lst = list(map(int, tokenizedInput[1:]))
    return triplets(n, lst)


def __starting_point():
    main()


__starting_point()
