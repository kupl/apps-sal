t = int(input())
while t:
    t = t - 1
    n = int(input())
    A = list(map(int, input().split()))
    z = 0
    sum = 0
    for x in A:
        if x > 0:
            sum += x
            z += 1
    V = A[:z]
    index = []
    for i in range(1, len(A) + 1):
        if i <= z:
            if A[i - 1] < 0:
                index.append(i)
        elif A[i - 1] > 0:
            index.append(i)
    if sum == 0:
        print(0)
        print(0)
    else:
        print(sum)
        print(len(index), end=' ')
        for x in index:
            print(x, end=' ')
        print()
