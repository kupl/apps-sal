for t in range(eval(input())):
 arr=list(map(int,input().split()))
 k=eval(input())
 m=-1
 if k<=arr[0]: m=0
 elif k<=arr[1]: m=1
 elif k<=arr[2]: m=2
 if k==1: print(1)
 else: print(min(k,arr[m%3])+min(k-1,arr[(m+1)%3])+min(k-1,arr[(m+2)%3]))
