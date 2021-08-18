def UCLN(a, b):
    while (a != b):
        if a > b:
            a = a // 2
        else:
            b = b // 2
    return a


def find_path(u, v):
    ucln = UCLN(u, v)
    arr1 = []
    arr2 = []
    while (u >= ucln):
        arr1.append(u)
        u = u // 2
    while (v > ucln):
        arr2.append(v)
        v = v // 2
    return arr1 + arr2[::-1]


p = int(input())
dic = {}

for i in range(p):
    value = list(map(int, input().split()))
    action = value[0]
    if action == 1:
        path = find_path(value[1], value[2])
        for i in range(len(path) - 1):
            if "{}{}".format(path[i], path[i + 1]) not in dic and "{}{}".format(path[i + 1], path[i]) not in dic:
                dic["{}{}".format(path[i], path[i + 1])] = value[3]
                dic["{}{}".format(path[i + 1], path[i])] = value[3]
            else:
                dic["{}{}".format(path[i], path[i + 1])] += value[3]
                dic["{}{}".format(path[i + 1], path[i])] += value[3]
    else:
        total = 0
        path = find_path(value[1], value[2])
        for i in range(len(path) - 1):
            if "{}{}".format(path[i], path[i + 1]) in dic:
                total += dic["{}{}".format(path[i], path[i + 1])]
        print(total)
