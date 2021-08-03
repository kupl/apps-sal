import string
a = input()
b = a.split()
n = int(b[1])
array = [0] * int(b[0])
for i in range(0, n):
    c = input()
    d = c.split()
    if d == ['CLOSEALL']:
        array = [0] * int(b[0])
    else:
        e = int(d[1])
        if array[e - 1] == 0:
            array[e - 1] = 1
        else:
            array[e - 1] = 0
    f = array.count(1)
    print(f)
