# cook your dish here
def Max_cust(T):
 for i in range(T):
  count = 0
  cus_prefer = {}
  n,k = map(int,input().split())
  for j in range(n):
   s,f,p=map(int, input().split())
   if p not in cus_prefer:
    cus_prefer[p] = [(s,f)]
   else :
    cus_prefer[p].append((s,f))
  for v in cus_prefer.values():
   v.sort(key = lambda x:x[1])
   previous = (0,0)
   for item in v:
    if item[0] >= previous[1]:
     previous = item
     count += 1
  print(count)

t = int(input())
Max_cust(t)
