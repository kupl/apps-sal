# cook your dish here

T = int(input())

for _ in range(T):
 n = int(input())
 s = 0
 temp = []
 for _ in range(n):
  l = list(map(int, input().split()))
  if l[0]%2 == 0:
   s += sum(l[1:len(l)//2+1])
  else:
   s += sum(l[1:len(l)//2])
   temp.append(l[len(l)//2])
 temp.sort(reverse= True)
 s += sum(temp[::2])
  
 print(s)

