n = int(input())
for i in range(n):
    count = 0
    k = input()
    x = list(k)
    kk = input()
    y = list(kk)
    for j in y:
        for jj in x:
            if(j == jj):
                count = count + 1
                break
    print(count)
