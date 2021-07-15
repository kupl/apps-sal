# cook your dish here
n = int(input())
sum1 = 0
sum2= 0
for i in range(0,n):
    arr=[]
  
    arr = list(map(int,input().split()))
    lst =  [arr[2]]
    for i in range(1,arr[1]):
        a = lst[-1]*arr[3]
        lst.append(a)
    total = sum(lst)
    diff = arr[0] - total
    if diff >=0:
        sum1 = sum1+diff
        print("POSSIBLE "+str(diff))
    else:
        sum2 = sum2+diff
        print("IMPOSSIBLE "+str(abs(diff)))
check = sum1+sum2
if check>=0:
    
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
