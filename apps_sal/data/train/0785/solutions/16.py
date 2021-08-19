def two(d):
    return 2 ** d - 1


for _ in range(int(input())):
    a = int(input())
    d = 1
    chef_acc = a * d - two(d)
    lst = []
    day = []
    while chef_acc >= 0:
        chef_acc = a * d - two(d)
        lst.append(chef_acc)
        day.append(d)
        d += 1
    print(day[-2], lst.index(max(lst)) + 1)
