def calc(X):
    for i in range(10):
        RET = []
        h = i
        l = 0
        for j in range(len(X)):
            if X[j] >= h:
                h = X[j]
                RET.append("2")
            elif l <= X[j] <= i:
                l = X[j]
                RET.append("1")
            else:
                break
        else:
            print("".join(RET))
            break
    else:
        print("-")

T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(a) for a in input()]
    calc(A)


