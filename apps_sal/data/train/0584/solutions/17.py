# cook your dish here
for _ in range(int(input())):
    s=input()
    lis=[]
    count=0
    for i in s:
        lis.append(int(i))
    
    if lis[0]==0:
            print(0)
            continue
    i=0
    while i<len(lis) and lis[i]==1:
        i+=1
        continue
    #print(i)
    while i<len(lis) and lis[i]==0:
        count+=1
        i+=1
    print(count)



