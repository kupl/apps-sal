# cook your dish here
NUMBER=input().split()
D1=int(NUMBER[0])
V1=int(NUMBER[1])
D2=int(NUMBER[2])
V2=int(NUMBER[3])
P=int(NUMBER[4])
number_vaccine=0
count=0
if D1>D2:
 count=D2-1
 number_vaccine=V2*(D1-D2)
 count+=D1-D2
 while(number_vaccine<P):
  number_vaccine+=V1+V2
  count+=1
 print(count)
elif D1==D2:
 count=D1-1
 number_vaccine=V1+V2
 count+=1
 while(number_vaccine<P):
  number_vaccine+=V1+V2
  count+=1 
 print(count)
else:
 count=D1-1
 number_vaccine=V1*(D2-D1)
 count+=D2-D1
 while(number_vaccine<P):
  number_vaccine+=V1+V2
  count+=1
 print(count)
