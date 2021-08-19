t = int(input())
for i in range(t):
    n = int(input())
    x = ''
    lst = []
    for j in range(n):
        x += input()
    lst.append(x.count('c') // 2)
    lst.append(x.count('e') // 2)
    lst.append(x.count('d'))
    lst.append(x.count('o'))
    lst.append(x.count('h'))
    lst.append(x.count('f'))
    print(min(lst))
