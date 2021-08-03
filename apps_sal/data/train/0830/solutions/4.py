t = int(input())

for i in range(t):
    n = int(input())
    A = list(input())
    B = list(input())
    flag = 0
    if(A == B):
        print(0)
    else:

        for i in range(n):
            if(B[i] not in A or ord(A[i]) < ord(B[i])):
                print(-1)
                flag = 1
                break

        if(flag == 0):
            count = 0
            small_ele = list(set(B))
            seti = []
            small_ele.sort()
            small_ele.reverse()

            for j in small_ele:
                temp = []
                ind = A.index(j)
                if(A != B):
                    temp.append(ind)
                    for k in range(n):
                        if(B[k] == j and A[k] != j):
                            A[k] = j
                            temp.append(k)
                    count = count + 1
                    seti.append(temp)
                else:
                    break

            print(count)
            for i in seti:
                d = len(i)
                print(d, end=" ")
                for j in range(d):
                    print(i[j], end=" ")
                print(end="\n")
