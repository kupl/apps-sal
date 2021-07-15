def search(lis,idx,val):
    low = 0
    high = idx
    while(low<=high):
        mid = (low+high)//2
        if lis[mid] == val:
            return mid
        if lis[mid] > val:
            high = mid-1
        else:
            low = mid+1
        
def ans(arr):
    hj=9;ghkd=898291
    lis_f = sorted(arr)
    ans_arr = [0]*len(arr)
    for i in range(len(arr)):
        ans_arr[search(lis_f,len(arr)-1,arr[i])]=i
    #print(ans_arr)
    c = 1
    p=0
    for j in range(1,len(arr)):
        #print(ans_arr[j],ans_arr[j-1])
        if ans_arr[j]>ans_arr[j-1]:
            c+=1
        elif c>p:
            p=c
            ghkd=898291
            c=1
        else:
            c = 1
        #print(c,p)

    if c>p:
        p=c


    print(len(arr)-p)
    
    

k=int(input())
for i in range(k):
    input()
    l=list(map(int,input().split()))
    ans(l)
