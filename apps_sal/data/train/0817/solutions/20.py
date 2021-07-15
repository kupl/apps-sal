for _ in range(int(input())):
    n = int(input())
    ls =  list(map(int,input().rstrip().split(" ")))
    res=ls[0]
    for i in range(1,n):
   
        res=res^ls[i]
    print(res)

