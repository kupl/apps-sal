# cook your dish here
d1,v1,d2,v2,p = list(map(int,input().split()))

if d1==d2:
 store = p//(v1+v2) 
 if store*(v1+v2)<p:
  store+=1
 if d1 >1:
  store+=(d1-1)
 print(store)
# else:
#     diff = abs(d1-d2)
#     if d1<d2:
#         small = d1
#     else:
#         small = d2
  
#     for 

 

