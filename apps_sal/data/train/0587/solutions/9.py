# cook your dish here
# cook your dish here
def solve():
  k = int(input())
    #n,m = input().split()
    #n = int(n)
    #m = int(m)
    #s = input()
  a = list(map(int, input().split()))
  #print(a)
  for i in range(k):
    n2=-1
    if a[i]==1 :n2 =3
    elif a[i]==2 :n2 =1
    else:
      b = bin(a[i]).replace("0b","")
      n = len(b)
      #print(b)
      if b[n-2]=='0': b=b[0:n-2]+'1'+b[n-1:]
      else: b=b[0:n-2]+'0'+b[n-1:]
      #print(b)
      n2 = int(b,2)
    #print(n2)
    if i==k-1:print(n2,end="")
    else: print(n2,end=" ")
        
            
    
    
def __starting_point():
    #T = int(input())
    #for i in range(T):
        #a = solve()
        #n = len(a)
        #for i in range(n):
         #   if i==n-1 : print(a[i])
          #  else: print(a[i],end=" ")
        (solve())
__starting_point()
