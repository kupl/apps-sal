# cook your dish here
def gcd(a, b):
    while True :
        if (b == 0): 
            return a
        c = b
        b = a%b
        a = c
testcase = int(input())
for tes in range(testcase) :
    n = int(input())
    arr = []
    left = [i for i in range(3, n+1, 2)]
    for i in range(2, n+1, 2) :
        arr.append([i])
    leng = len(arr)
    if n > 1 :
        arr[0].append(1)
    if n == 1 :
        arr.append([1])
    num = 0
    np = 3
    while len(left) > 0 :
        if num == 0 or num > n :
            num = left[0]
            pnum = num
            i = 0
            p = np
            np += 2
        if num in left :
            left.remove(num)
            flag1 = False
            while i<len(arr) :
                flag2 = True
                for j in arr[i] :
                    if num%j==0 or ( j!=1 and gcd(num, j) != 1) :
                        flag2 = False
                        break
                if flag2 :
                    arr[i].append(num)
                    num = (p*pnum)
                    p += 2
                    flag1 = True
                    break
                i += 1
            if not flag1 :
                arr.append([i])
                num = (p*pnum)
                p += 2
        else :
            num = (p*pnum)
            p += 2
    print(len(arr))
    for ele in arr :
        print(len(ele), end=' ')
        for i in ele :
            print(i, end=' ')
        print()
