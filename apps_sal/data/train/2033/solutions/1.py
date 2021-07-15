n=int(input())

a=list(map(int,input().split()))

p=[]

q=[]

r=0

ls=-1

for i in a:

    for j in range(i):

        p.append(r)

        if j:q.append(r-(ls>1))

        else:q.append(r)

    r+=i

    ls=i

if p==q:print('perfect')

else:

    print('ambiguous')

    print(*p)

    print(*q)



# Made By Mostafa_Khaled

