t = eval(input())
mn = []
army = []
for i in range(0, t):
    temp = input()
    a, b = temp.split()
    a = int(a)
    b = int(b)
    mn.append((a, b))
    temp = input()
    new = [int(i) for i in temp.split()]
    army.append(new)

for i in range(0, t):
    n = mn[i][0]
    m = mn[i][1]
    li = army[i]
    s = 0
    for j in range(0, len(li)):
        if(j < m):
            s += li[j]
        else:
            s -= (li[j] / 2)
    if(s >= 0):
        print("VICTORY")
    else:
        print("DEFEAT")
