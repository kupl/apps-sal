for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))[:n]
    m = int(input().strip())
    list1=[]
    list2=[]
    for i in range(0,n):
        arr[i]= (arr[i]+arr[i]%3)
        if arr[i]>m:
            list1.append(arr[i])
        if arr[i]<m:
            list2.append(arr[i])
    if len(list1)>0 and len(list2)>0:
          print(max(list2),min(list1))
    elif len(list1)<=0 and len(list2)>0:
        print(max(list2),"-1")
    elif len(list1)>0 and len(list2)<=0:
        print("-1",min(list1))
    else:
        print("-1","-1")
