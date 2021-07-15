for _ in range(int(input())):
    N=list(input().strip())
    a=N.count('4')
    b=N.count('7')
    print(len(N)-a-b)
