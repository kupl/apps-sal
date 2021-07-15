x = int(input())
li = []
for i in range(x):
    temp = 0
    s,n,k,r = map(int, input().split())
    for j in range(n):
        if j == 0:
            temp += k
        else:
            k = k*r 
            temp += k
    if temp > s:
        print("IMPOSSIBLE {0}".format(temp-s))
        li.append(s-temp)
    else:
        print("POSSIBLE {0}".format(s-temp))
        li.append(s-temp)
if sum(li) >= 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
