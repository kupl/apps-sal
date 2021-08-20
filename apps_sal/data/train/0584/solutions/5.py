t = int(input())
for i in range(t):
    count = 0
    x = list(input())
    f1 = 0
    f2 = 0
    for i in range(len(x)):
        if x[i] == '1' and f1 == 0 and (f2 == 0):
            f1 = 1
        elif x[i] == '1' and f1 == 1 and (f2 == 0):
            continue
        elif x[i] == '0' and f1 == 0 and (f2 == 0):
            f2 = 1
        elif x[i] == '0' and f1 == 1:
            count = count + 1
            f2 = 2
        elif x[i] == '0' and f2 == 1:
            continue
        elif x[i] == '0' and f2 == 2:
            count = count + 1
        elif x[i] == '1' and f2 == 1:
            break
        elif x[i] == '1' and f2 == 2:
            break
    print(count)
