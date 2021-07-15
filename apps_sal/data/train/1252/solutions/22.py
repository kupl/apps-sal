for t in range(int(input())):
    n = int(input())
    A = [True for i in range(n+1)]
    A[0],A[1] = False,False
    i = 2
    while i**2 <= n:
        if A[i] == True:
            for j in range(i**2,n+1,i):
                A[j] = False
        i += 1
    sum = 0
    for i in range(2,n+1):
        if A[i] == True:
            sum += i
            if sum >= 10:
                sum %= 10
    print(sum)
