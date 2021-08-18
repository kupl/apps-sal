n = int(input())

while n != 0:
    no, b = list(map(int, input().split()))
    v = list(map(int, input().split()))
    number = sum(v) / no
    count = 0
    flag = True
    values = []
    if ((sum(v) % no) != 0) or (b > no):
        flag = False
    for i in range(b):
        vals = []
        for j in range(i, len(v), b):
            vals.append(v[j])
        values.append(vals)
    for i in range(len(values)):
        if sum(values[i]) / len(values[i]) != number:
            flag = False
    if flag:
        for i in range(no - b):
            y = v[i] - number
            v[i] -= y
            v[i + b] += y
            count += abs(y)

        print(count)
    else:
        print("-1")
    n = n - 1
