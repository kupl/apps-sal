# cook your dish here
for _ in range(int(input())):
 n = int(input())
 l = list(map(int, input().split()))
 t_sum = 0
 count = 0
 for i in range(n):
  if l[i] >= 0:
   t_sum += l[i]
   count += 1


 print(t_sum)
 if count == n or count==0:
  print(0)
 else:
  index_1 = []
  index_2 = []
  i = 0
  j = len(l)-1
  while i<j:
   while i<n and l[i] < 0:
    i+=1
   while j>-1 and l[j] > 0:
    j-=1
   if i<j:
    index_1.append(i+1)
    index_2.append(j+1)
    i+=1
    j-=1
  index_2.reverse()
  print(len(index_1)+len(index_2) , *index_1, *index_2)
