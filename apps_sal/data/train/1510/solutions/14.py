t = int(input())
while t > 0:
    lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    n = input()
    op = 0
    for i in n:
        if i in lst:
            op += 1
    print(op)
    t -= 1
