try:
 # cook your code here
 for _ in range(int(input())):
  a=int(input())
  if a<=250000:
   print(a)
  elif a<=500000:
   res=a-((a-250000)*(0.05))
   print(int(res))
  elif a<=750000:
   res=a-(12500+(a-500000)*(0.1))
   print(int(res))
  elif a<=1000000:
   res=a-(12500+25000+(a-750000)*(0.15))
   print(int(res))
  elif a<=1250000:
   res=a-(12500+25000+37500+(a-1000000)*(0.2))
   print(int(res))
  elif a<=1500000:
   res=a-(12500+25000+37500+50000+(a-1250000)*(0.25))
   print(int(res))
  else:
   res=a-(12500+25000+37500+50000+62500+(a-1500000)*(0.3))
   print(int(res))
except:
 pass
