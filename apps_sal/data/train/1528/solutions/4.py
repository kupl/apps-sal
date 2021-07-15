for _ in range(int(input())):
 n,k = list(map(int,input().split()))
 arr =input().split()

 for i in range(k):
  if arr[-1]=="H":
   arr.pop()
   n=n-1
   for j in range(n):
    if arr[j]=="H":
     arr[j]="T"
    else:
     arr[j]="H"
  else:
   arr.pop()
   n=n-1
 print(arr.count("H"))
   

