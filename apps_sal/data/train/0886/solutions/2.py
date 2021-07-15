for _ in range(int(input().strip())):
    n = int(input().strip())
    list1 = list(map(int, input().strip().split()))[:n]
    m = int(input().strip())
    for i in range(n):
        list1[i] = list1[i] + list1[i]%3
    #print(list1)
    l1 = []
    l2 = []
    list2 = sorted(list1)
    for i in range(n-1,0,-1):
        if list2[i]>m:
            l1.append(list2[i])
    for i in range(n):
        if list2[i]<m:
            l2.append(list2[i])
    if len(l1)>0 and len(l2)>0:
        print(max(l2),min(l1))
    elif len(l1)<=0 and len(l2)>0:
        print(max(l2),"-1")
    elif len(l1)>0 and len(l2)<=0:
        print("-1",min(l1))
    else:
        print("-1","-1")
