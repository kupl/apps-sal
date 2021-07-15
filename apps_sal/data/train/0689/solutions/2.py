s1,s2=[],[]
flag=0
for _ in range(int(input())):
    x,y=[int(x) for x in input().split()]
    s1.append(x)
    s2.append(x+y)
for _ in range(len(s1)):
    for __ in range(len(s2)):
        if _!=__ and s1[__]==s2[_] and s1[_]==s2[__]:
            flag=1
            print('YES')
            break
    if flag==1:
        break
if flag==0:
    print('NO')

