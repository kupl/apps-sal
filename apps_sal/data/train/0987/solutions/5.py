# cook your dish here
t=int(input())
for i in range(t):
 fin,disttobol,tigacc,bolspeed=list(map(int,input().split()))
 boltime=fin/bolspeed
 tigtime=(((fin+disttobol)*2)/tigacc)**(1/2)
 if(boltime<tigtime):
  print("Bolt")
 else:
  print("Tiger")

