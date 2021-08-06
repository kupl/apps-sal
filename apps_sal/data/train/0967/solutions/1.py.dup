# cook your dish here
try:
    def countsubsetsum(S, arr, n):
        k = [[0 for i in range(S + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(S + 1):
                if(j == 0):
                    k[i][j] = 1
                elif(i == 0):
                    k[i][j] = 0
                elif(arr[i - 1] <= j):
                    k[i][j] = k[i - 1][j - arr[i - 1]] + k[i - 1][j]
                else:
                    k[i][j] = k[i - 1][j]
        return k[n][S]
    for _ in range(int(input())):
        m = int(input())
        S = int(input())
        arr = [int(i) for i in input().split()]

        n = len(arr)

        print(countsubsetsum(S, arr, n))
except EOFError as e:
    pass
