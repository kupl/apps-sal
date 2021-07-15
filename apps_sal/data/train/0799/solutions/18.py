test_case=int(input())
re=0
for i in range(test_case):
 a=list(map(int,input().split()))
 cunt=a.count(1)
 if cunt>=2:
  re=re+1 
print(re)
  
 

