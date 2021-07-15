# cook your dish here
import math as m
NUMBER=input().split()
D1=int(NUMBER[0])
V1=int(NUMBER[1])
D2=int(NUMBER[2])
V2=int(NUMBER[3])
P=int(NUMBER[4])
number_vaccine=0
count=0
if D1>D2:
 print(D1-1+m.ceil((P-V2*abs(D1-D2))/(V1+V2)))
elif D1==D2:
 count=D1-1
 print(D1+m.ceil(P/(V1+V2))-1)
else:
 print(D2-1++m.ceil((P-V1*abs(D1-D2))/(V1+V2)))
