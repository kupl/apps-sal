inp = input().split()
(row_n, col_m, operation_p) = (int(inp[0]), int(inp[1]), int(inp[2]))
operations = []
for i in range(operation_p):
    inp = input().split()
    (row, col) = (int(inp[0]), int(inp[1]))
    operations.append([row, col])
operations.sort()
i = 0
sol_index = 1
while i < operation_p:
    if operations[i][0] == sol_index:
        sol = col_m - 1
        o = {}
        while i < operation_p and operations[i][0] == sol_index:
            e = operations[i][1]
            if e in o:
                o[e] += 1
            else:
                o[e] = 1
            i += 1
        for e in o:
            if o[e] > 1:
                if e + 1 <= col_m:
                    if e + 1 in o:
                        if o[e] - o[e + 1] > 1:
                            sol = -1
                            break
                    else:
                        sol = -1
                        break
        if sol != -1:
            if 1 in o:
                sol -= o[1]
            if col_m in o:
                sol += o[col_m]
        print(sol)
        sol_index += 1
    else:
        print(col_m - 1)
        sol_index += 1
while sol_index <= row_n:
    print(col_m - 1)
    sol_index += 1
