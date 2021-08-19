from sys import stdout
def intput(): return [int(i) for i in input().split()]


# Write your code here
sol = "3332323313233322223333"
subsets = ['100', '010', '001', '110', '101', '011', '111']
def eq(x, y): return abs(x - y) < 1e-6


def check(x):
    if x == [9, 7, 4]:
        print("Debug")
    if x == y:
        return 0
    d, q, f = [], [], []
    for i in range(3):
        d.append(y[i] - x[i])
        q.append(0.5 if x[i] == 0 else y[i] / x[i])
        f.append(q[i] % 1 == 0)
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        if x[j] == y[j] and x[k] == y[k]:
            return 1
        if x[i] == y[i] and (d[j] == d[k] or (f[j] and eq(q[j], q[k]))):
            return 1
    if (d[0] == d[1] and d[0] == d[2]) or (f[0] and eq(q[0], q[1]) and eq(q[0], q[2])):
        return 1
    return 2


def move(subset, oper, d):
    res = x.copy()
    for i in range(3):
        if subset[i] == '1':
            res[i] = res[i] + d if oper else res[i] * d
    return res


for tc in range(int(input())):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    a = check(x)
    if a < 2:
        print(a)
        continue
    d, q, f = [], [], []
    for i in range(3):
        d.append(y[i] - x[i])
        q.append(0.5 if x[i] == 0 else y[i] / x[i])
        f.append(q[i] % 1 == 0)
    flag = False
    for subset in subsets:
        for i in range(3):
            a = check(move(subset, True, d[i]))
            if a < 2:
                print(2)
                flag = True
                break
            if f[i]:
                a = check(move(subset, False, q[i]))
                if a < 2:
                    print(2)
                    flag = True
                    break
        if flag:
            break
    if flag:
        continue
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        if x[j] != 0 and x[k] != 0 and eq((y[j] - d[i]) / x[j], (y[k] - d[i]) / x[k]) and ((y[j] - d[i]) / x[j]) % 1 == 0:
            print(2)
            flag = True
            break
    if flag:
        continue
    if x[0] != x[1] and eq((y[0] - y[1]) / (x[0] - x[1]), (y[0] - y[2]) / (x[0] - x[2])):
        print(2)
        continue
    print(3)
