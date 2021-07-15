def func(mas, n, m):
    flag1=0
    flag2=n-1
    i=0
    j=1
    while(i<m):
        if(mas[i][1]==1):
            tmp = mas[i][0]-1
            while(j<mas[i][0]):
                if(mas[i][j]==mas[i][j+1]-1):
                    flag2-=1
                    tmp-=1
                else:
                    break
                j+=1
            flag1+=tmp
        else:
            flag1=flag1+mas[i][0]-1
        i+=1
    return flag1+flag2
n,m = map(int, input().split())
mas=[[]for i in range(m)]
h=0
for i in mas:
    s = input()
    p = s.split()
    while h<len(p):
        i.append(int(p[h]))
        h+=1
    h=0
print(func(mas,n,m))
