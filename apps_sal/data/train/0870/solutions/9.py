T = int(input())
for _ in range(T):
    s = input()
    l = []
    a = 0
    b = 0
    for i in s:
        if i == '1':
            if a != 0:
                l.append(a)
                a = 0
            b += 1
        else:
            if b != 0:
                l.append(b)
                b = 0
            a -= 1
    if a != 0:
        l.append(a)
    if b != 0:
        l.append(b)
    A = [0]
    B = [0]
    for i in l:
        if i < 0:
            A.append(-i + A[-1])
            B.append(B[-1])
        else:
            A.append(A[-1])
            B.append(i + B[-1])
    m = 0
    x = len(A) - 1
    for i in range(1, x + 1):
        for j in range(i, x + 1):
            m = max(m, A[j] - A[i - 1] + B[i - 1] + B[x] - B[j], B[j] - B[i - 1] + A[i - 1] + A[x] - A[j])
    print(len(s) - m)
