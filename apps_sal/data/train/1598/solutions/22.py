def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


t = int(input())
while(t):
    t -= 1
    avg = 0
    x = []
    y = []
    z = []

    n = int(input())
    for i in range(0, n):
        a, b, c = input().split(' ')
        c = int(c)
        x.append(a)
        y.append(b)
        z.append(c)
        avg = avg + c
    avg = avg / n
    '''for i in range(0,n):
     for j in range(0,n):
      if z[i]>z[j]:
       swapPositions(z,i,j)
       swapPositions(x,i,j)
       swapPositions(y,i,j)'''
    for i in range(0, n):
        if z[i] < avg:
            print(x[i] + " " + y[i] + " " + str(z[i]))
