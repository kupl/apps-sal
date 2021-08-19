(a, b, c, d) = input().split(' ')
A = []
A.append(float(a))
A.append(float(b))
A.append(float(c))
A.append(float(d))
A.sort()
if A[0] / A[1] == A[2] / A[3]:
    print('Possible')
elif A[0] / A[2] == A[1] / A[3]:
    print('Possible')
elif A[0] / A[3] == A[1] / A[2]:
    print('Possible')
else:
    print('Impossible')
