for tests in range(eval(input())):
    n = eval(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    pro = 0
    index = 0
    tmp = 1
    r = 0
    for i in range(n):
        tmp = L[i] * R[i]
        if tmp > pro:
            pro = tmp
            index = i + 1
        if tmp == pro:
            if R[i] > r:
                index = i + 1
                r = R[i]
    print(index)
