t=int(input())

def gcd(a,b):
 if a<b:
  a=a+b
  b=a-b
  a=a-b

 if a%b==0:
  return b
 else:
  c=a%b
  return gcd(b,c)

for _ in range(t):
 n=int(input())
 angle_list=list(map(int,input().split()))
 slice_list=[]
 for i in range(n):
  if i==n-1:
   theta=angle_list[0]+360-angle_list[i]
  else:
   theta=angle_list[i+1]-angle_list[i]
  slice_list.append(theta)
 for i in range(n-1):
  slice_list[1]=gcd(slice_list[0],slice_list[1])
  slice_list.pop(0)
 slices=360/slice_list[0]-n
 print(str(int(slices)))

