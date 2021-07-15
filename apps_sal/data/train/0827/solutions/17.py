t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = input()
    na = s.count('a')
    nb = s.count('b')
    temp =nb
    #print(na,nb)
    summ = 0
    for i in range(len(s)):
        if(s[i]=='a'):
            summ += nb
        elif(s[i]=='b'):
            nb -=1
        else:
            pass
    #print(summ)
    ans = summ*k + ((k*(k-1))//2)*na*temp
    print(ans)

