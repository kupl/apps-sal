n, k = list(map(int, input().strip().split()))
A = list(map(int, input().strip().split()))
s = sum(A)
t = s // k
if(s % t != 0):
    print("No")
else:
    final = []
    i = 0
    flag = True
    while(i != n):
        s1 = 0
        temp = []

        while(s1 < t and i < n):
            s1 += A[i]
            temp.append(A[i])
            i += 1
        if(s1 != t):
            flag = False
            break
        else:
            final.append(len(temp))

    if(flag is False):
        print("No")
    else:
        print("Yes")
        print(' '.join(list(map(str, final))))
