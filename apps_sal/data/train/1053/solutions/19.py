# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    lst = list(map(int,input().split()))
    count = 0
    lst.sort()
    for j in lst:
        if j == 0 :
            count = count+1 
    print(count)        

