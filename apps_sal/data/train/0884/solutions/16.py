for t in range(int(input())):
    (X, K) = input().split()
    (X, K) = (int(X), int(K))
    l = []
    l1 = []
    for i in range(2, X + 1):
        if X % i == 0:
            l.append(i ** K)
    for j in range(2, K + 1):
        if K % j == 0:
            l1.append(j * X)
    print(sum(l), sum(l1))
