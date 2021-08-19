# cook your dish here
t = int(input())
for s in range(t):
    n = int(input())
    if(n % 2 == 0):
        print('NO')
    else:
        print('YES')
        a = [[0 for i in range(n)]for i in range(n)]
        i = 0
        j = 1
        k = 1
        while(k < n):
            i = 0
            j = k
            while(i < n and j < n):
                a[i][j] = 1
                i += 1
                j += 1
            k += 2
        i = 1
        j = 0
        k = 1
        while(k < n):
            i = k
            j = 0
            while(i < n and j < n):
                if(a[j][i] == 0):
                    a[i][j] = 1
                i += 1
                j += 1
            k += 1
        for i in range(n):
            for item in a[i]:
                print(item, end="")
            print(" ")
