T = int(input())
for i in range(0,T):
    N = input().strip()
    cnt=0
    for j in range(0,len(N)):
        if N[j]!='4' and N[j]!='7':
            cnt +=1
    print(cnt)

