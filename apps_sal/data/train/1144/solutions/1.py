def r():
 return list(map(int,input().split()))
def process(stack):
 if len(stack)<k+1:
  ans.extend(stack)
  return
 # print stack,
 # nonlocal count
 if len(stack)%(k+1)==0:
  # print "as"
  for i in range(k,len(stack)-1,k+1):
   stack[i]=(stack[i]+1)%2
  stack[-2]=(stack[-2]+1)%2
 else:
  for i in range(k,len(stack),k+1):
   # print i
   stack[i]=(stack[i]+1)%2
 # count+=((len(stack)+k)/(k+1))
 # print stack
 ans.extend(stack)
for i in range(eval(input())):
 n,k = r()
 arr = list(map(int,list(input())))
 if k==1:
  s=[]
  c=0
  for i in range(n):
   s.append((c+1)%2)
   c+=1
  s1=[]
  c=1
  for i in range(n):
   s1.append((c+1)%2)
   c+=1
  ans1,ans2=0,0
  for i in range(n):
   if arr[i]!=s1[i]:
    ans2+=1
   if arr[i]!=s[i]:
    ans1+=1
  s1=list(map(str,s1))
  s=list(map(str,s))
  if ans1<ans2:
   print(ans1)
   print(''.join(s))
  else:
   print(ans2)
   print(''.join(s1))
 else:
  # print japasas
  ans=[]
  c=1
  count=0
  stack=[arr[0]]
  for i in range(1,n):
   if arr[i]==arr[i-1]:
    stack.append(arr[i])
   else:
    process(stack)
    stack=[arr[i]]
  # ans.extend(stack)
  process(stack)
  count=0
  for i in range(n):
   if ans[i]!=arr[i]:
    count+=1
  print(count)
  ans=list(map(str,ans))
  print(''.join(ans))
