t = int(input())
for i in range(t):
    (r, c) = map(int, input().split())
    arr = [['' for x in range(c)] for y in range(r)]
    for j in range(r):
        arr[j] = list(str(input()))
    anr = ['U', 'D', 'L', 'R']
    meet = 0
    pos = [[[0 for z in range(c)] for y in range(r)] for x in range(max(r, c))]
    j = 0
    k = 0
    while j < r:
        j_init = j
        k = 0
        while k < c:
            k_init = k
            if arr[j][k] in anr:
                for z in range(max(r, c)):
                    if j == r or k == c or arr[j][k] == '#' or (k == -1) or (j == -1):
                        break
                    if pos[z][j][k] > 0:
                        meet += pos[z][j][k]
                    pos[z][j][k] += 1
                    if arr[j_init][k_init] == 'D':
                        j += 1
                    elif arr[j_init][k_init] == 'U':
                        j -= 1
                    elif arr[j_init][k_init] == 'L':
                        k -= 1
                    elif arr[j_init][k_init] == 'R':
                        k += 1
            k = k_init + 1
            j = j_init
        j = j_init + 1
    print(meet)
