from math import sqrt


def distance_between_two_points(point1, point2):
    a = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    return round(sqrt(a), 10)


for _ in range(int(input())):
    blank = input()
    N = int(input())
    dic = {}
    array = []
    for i in range(N):
        (x, y) = map(int, input().split())
        if x not in dic.keys():
            dic[x] = len(array)
            array.append([x, y, y])
        else:
            index = dic[x]
            array[index][1] = min(y, array[index][1])
            array[index][2] = max(y, array[index][2])
    array.sort()
    ans = 0
    length = len(array)
    for i in range(len(array) - 1):
        ini = array[i]
        fin = array[i + 1]
        ans += ini[2] - ini[1]
        ans += distance_between_two_points([ini[0], ini[1]], [fin[0], fin[2]])
    ans += array[-1][2] - array[-1][1]
    print('{:0.2f}'.format(ans))
