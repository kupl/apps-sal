# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    array=list(map(int, input().split()))
    list_sub=[]
    idx=0
    counter=0
    for i in range(n-1):
        if counter%2==0 and array[i]<=array[i+1]:
            counter+=1 
        elif counter%2==1 and array[i]>=array[i+1]:
            counter+=1 
        else:
            list_sub.append((idx,i))
            if counter%2==1:
                idx=i 
                counter=1
            else:
                idx=i+1 
                counter=0
    list_sub.append((idx, n-1))
    massimo=0
    if len(list_sub)==1:
        massimo=list_sub[0][1]-list_sub[0][0]+2
    for i in range(len(list_sub)-1):
        if list_sub[i][1]==list_sub[i+1][0]:
            massimo=max(massimo, list_sub[i][1]-list_sub[i][0]+2+list_sub[i+1][1]-list_sub[i+1][0])
        else:
            massimo=max(massimo, list_sub[i][1]-list_sub[i][0]+3+list_sub[i+1][1]-list_sub[i+1][0])
    print(massimo)
