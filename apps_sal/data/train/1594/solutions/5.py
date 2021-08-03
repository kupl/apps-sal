# cook your dish here
# cook your dish here
for _ in range(int(input())):
    size = int(input())
    power = []
    for i in range(size):
        power.append(input())
    diag = True
    for i in range(size):
        if power[i][i] == '0':
            diag = False
            break
    if diag:
        print((size * (size + 1)) // 2)
    else:
        print(size)
