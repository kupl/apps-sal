testcases = int(input())
for testcase in range(testcases):
    temparr = input()
    temparr = temparr.split()
    x = int(temparr[0])
    y = int(temparr[1])
    n = int(temparr[2])
    if x == y:
        print(0)
        continue
    binaryx = "{0:b}".format(x)
    binaryy = "{0:b}".format(y)
    nx = len(binaryx)
    ny = len(binaryy)
    maxlen = max(nx, ny)
    binaryx = (maxlen - nx) * "0" + binaryx
    binaryy = (maxlen - ny) * "0" + binaryy
    binaryn = "{0:b}".format(n)
    index = 0
    flag = 0
    for i in range(maxlen):
        if binaryx[i] == binaryy[i]:
            continue
        index = i
        if binaryy[i] == "0":
            flag = 1
            break

        break
    arr = []
    for i in range(maxlen):
        if i == index:
            arr.append("1")
        else:
            arr.append("0")
    newstrs = "".join(arr)
    compareresult = int(newstrs, 2)
    ans = 0
    for i in range(n + 1):
        if flag == 1 and (i & compareresult):
            ans += 1
        if flag == 0 and (i & compareresult == 0):
            ans += 1

    print(ans)
