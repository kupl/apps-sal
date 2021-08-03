''' PROBLEM A  '''


'''   PROBLEM B   '''


'''   PROBLEM C   '''


'''   PROBLEM D    '''


n = int(input())
for i in range(0, n):
    p = input().rstrip().split(' ')
    # print(int(p[0]) * int(p[1]))
    q = input().rstrip().split(' ')
    x = int(p[1])
    q.sort(key=int)
    A = int(q[0])
    B = int(q[len(q) - 1])
    C = abs(A - B)
    if C < x:
        print("YES")
    else:
        print("NO")
