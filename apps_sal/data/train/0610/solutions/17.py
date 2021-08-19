# cook your dish here
for _ in range(int(input())):
    N = int(input())
    inp_lst = tuple(i for i in input().strip().split(' '))
    idx_lst = []
    printStr = 'YES'
    for i in range(N):
        if(inp_lst[i] == '1'):
            idx_lst.append(i)

    for i in range(1, len(idx_lst)):
        if(idx_lst[i] - idx_lst[i - 1] < 6):
            printStr = 'NO'
            break

    print(printStr)
