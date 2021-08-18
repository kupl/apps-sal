import sys
n, m, c = [int(i) for i in input().split()]
matrix = [[0] * (m + 1) for i in range(n + 1)]
cc = 1
nn = 1
mm = 1
'''
for nn in xrange(1,n+1) :
    for mm in xrange(1,m+1) :
        if cc <= c :
            print "2",
            print nn,nn,mm,mm
            sys.stdout.flush()
            matrix[nn][mm] = int(raw_input())
            cc += 1
        else :
            break
    if cc > c :
        break

for nnn in range(nn, n + 1):
    for mmm in range(mm, m + 1):

        x = 1
        y = 25
        z = 51
        while matrix[nnn][mmm] == 0:
            if cc < 499990:
                if abs(x - y) == 1:
                    print("1", end=' ')
                    print(nnn, nnn, mmm, mmm, x, x)
                    sys.stdout.flush()
                    cc += 1
                    value = int(input())
                    if value == 1:
                        matrix[nnn][mmm] = x
                    else:
                        matrix[nnn][mmm] = y
                    break
                else:
                    print("1", end=' ')
                    print(nnn, nnn, mmm, mmm, x, y)
                    sys.stdout.flush()
                    cc += 1
                    value = int(input())
                    if value == 1:
                        z = y
                        y = (x + y) / 2
                    else:
                        x = y
                        y = (y + z) / 2

            else:
                break

    if cc >= 499980:
        break
print("3")
sys.stdout.flush()
for nn in range(1, n + 1):
    for mm in range(1, m + 1):
        if matrix[nn][mm] < 1 or matrix[nn][mm] > 50:
            print("25", end=' ')
        else:
            print(matrix[nn][mm], end=' ')
    sys.stdout.flush()
    print()
