# cook your dish here

def foo(temp, p):
    flag = True
    for d in range(p):
        yet = temp[d]
        if 1 not in yet:
            flag = False
            break
    return flag


T = int(input())
for t in range(T):
    N = int(input())
    lst = []
    count = 0
    temp = []
    for n in range(N):
        num = list(map(int, str(input())))
        x = num.index(1)
        y = (n, x)
        temp.append(y)
        lst.append(num)

    print(int(N * (N + 1) / 2))
