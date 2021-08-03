# cook your dish here
for _ in range(int(input())):
    N = int(input())
    inp_arr = tuple(int(i) for i in input().strip().split())
    fine = 0
    maxMaint = 1000 * N
    for i in range(N):
        if(inp_arr[i] == 0):
            if(fine == 0):
                fine = 100 * (N - i)
        else:
            maxMaint -= 1000

    print(maxMaint + fine)
