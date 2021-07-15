# cook your dish here
series=[]
series.append(0)
i=1
j=2
for i in range(1,10000007):
 series.append(i*i+j*j*j)
 i=i+1
 j=j+1
 
t=int(input())
while t>0:
 n=int(input())
 print(series[n-1]%1000000007) 
 t=t-1

