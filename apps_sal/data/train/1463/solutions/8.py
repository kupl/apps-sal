def gcd(a, b): 
    if (b == 0): 
         return a 
    return gcd(b, a%b)

testcase = int(input())
for tes in range(testcase) :
    n = int(input())
    arr = []
    for i in range(2, n+1, 2) :
        arr.append([i])
    leng = len(arr)
    for i in range(1, n+1, 2) :
        flag1 = False
        for j in range(leng) :
            flag2 = True
            for k in arr[j] :
                if gcd(i, k) != 1 and i!=1 and k!=1 :
                    flag2 = False
                    break
            if flag2 :
                arr[j].append(i)
                flag1 = True
                break
        if not flag1 :
            arr.append([i])
            leng += 1
    print(len(arr))
    for ele in arr :
        print(len(ele), end=' ')
        for i in ele :
            print(i, end=' ')
        print()
