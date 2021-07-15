
t = int(input())
while(t>0 ):
 n= int(input())
 #b = [0]*n;
 B=list(map(int,input().strip().split(' ')))
 P=list(map(float,input().strip().split(' ')))
 l = [0]*32
 ans = 0 
 cur_bit = 1
 for i in range(0,31):
  # print(cur_bit,end =" ")
  cur_prob = 0.0
  for j in range(0,len(B)):
   if(cur_bit&B[j]):
    cur_prob = cur_prob*(1-P[j]) + (1-cur_prob)*P[j]
  cur_bit = cur_bit << 1
  # print(cur_prob)
  ans = ans + cur_prob* (2**i)

 print(ans)


 t-=1;
