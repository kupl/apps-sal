t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    arr = [[""for x in range(c)]for y in range(r)]
    for j in range(r):
        arr[j] = list(str(input()))
    # for j in range(r):
    #     print(arr[j])
    # anrnum=0
    anr = ['U', 'D', 'L', 'R']
    # for j in range(r):
    #     for k in range(c):
    #         if(arr[j][k]in anr):
    #             anrnum+=1
    meet = 0
    pos = [[[0 for z in range(c)] for y in range(r)] for x in range(max(r, c))]
    j = 0
    k = 0
    while j < r:
        j_init = j
        # if(j==r):
        # print("Fault:"+str(j))
        k = 0
        while k < c:
            k_init = k
            # if(j==r or k==c):
            #     print("Fault:"+str(j)+" "+str(k))
            # print(str(j) + " " + str(k))
            if(arr[j][k] in anr):

                for z in range(max(r, c)):
                    if(j == r or k == c or arr[j][k] == "#" or k == -1 or j == -1):
                        break
                    if(pos[z][j][k] > 0):
                        meet += pos[z][j][k]
                    # else:
                        # print(str(z) + " " + str(j) + " " + str(k))
                    pos[z][j][k] += 1
                    if(arr[j_init][k_init] == 'D'):
                        j += 1
                    elif(arr[j_init][k_init] == 'U'):
                        j -= 1
                    elif (arr[j_init][k_init] == 'L'):
                        k -= 1
                    elif (arr[j_init][k_init] == 'R'):
                        k += 1
            k = k_init + 1
            j = j_init
        j = j_init + 1
    print(meet)
    # for iter in range(max(r,c)):
    #     print(pos[iter])
