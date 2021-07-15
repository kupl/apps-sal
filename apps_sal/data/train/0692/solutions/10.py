def na(l,r):
 if l-1>=r or l>n or r>n:
  return True
 else:
  return False

def na_print():
 print('NA')



def func(t,l,r):
 if t=='U':
  a[l-1]=r
  return ''
 elif na(l,r):
  na_print()
  return ''
 
 if t=='A':
  print(sum(a[l-1:r]))
  
 elif t=='M':
  print(max(a[l-1:r]))
  
 elif t=='m':
  print(min(a[l-1:r]))
  
 elif t=='S':
  bb = list(set(a[l-1:r]))
  bb.sort()
  print(bb[-2])
  
 elif t=='s':
  bb = list(set(a[l-1:r]))
  bb.sort()
  print(bb[1])
  
 else:
  print('!!!')




n = eval(input())
a = list(map(int, input().split()))
q = eval(input())

for i in range(q):
 t,l,r = input().split()
 func(t,int(l),int(r))

