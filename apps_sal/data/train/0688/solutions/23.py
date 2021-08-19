t = int(input())
for T in range(t):
    n = input()
    lenn = len(n)
    oz = 0
    zo = 0
    for i in range(lenn - 1):
        if n[i] == '0' and n[i + 1] == '1':
            zo += 1
        elif n[i] == '1' and n[i + 1] == '0':
            oz += 1
        else:
            pass
    if n[lenn - 1] == '1' and n[0] == '0':
        oz += 1
    elif n[lenn - 1] == '0' and n[0] == '1':
        zo += 1
    else:
        pass
    if oz + zo <= 2:
        print('uniform')
    else:
        print('non-uniform')
