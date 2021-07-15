def distribute(nodes, workload):
    a=[[0] for x in range(nodes)]
    w=workload
    k=workload//nodes
    for j in range(0,workload%nodes):
     a[j][0]+=1
    for i in range(0,len(a)):
     for j in range(0,k):
      a[i][0]+=1
    total=0
    b=[[] for x in range(nodes)]
    for j in range(0,len(a)):
     for i in range(total, total+a[j][0]):
         b[j].append(i)
     total+=a[j][0]
    return b


