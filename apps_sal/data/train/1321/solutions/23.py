for _ in range(int(input())):
    n = int(input())
    n = n - 1
    answer = n*(n+1)*(2*n+1)//6
    print(answer)
