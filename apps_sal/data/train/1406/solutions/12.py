from sys import stdin,stdout
def main():
 t=int(stdin.readline())
 for i in range(t):
  list2=[]
  n,q=map(int,stdin.readline().split()) 
  a=list(map(int,stdin.readline().split()))
  for i in range(len(a)):                     
   list2.append((bin(a[i])).count("1"))
  o=0
  e=0
  for i in range(len(list2)):
    if((list2[i]%2)==0):
     e+=1
    else:
     o+=1
  for i in range(q):                          
   b=0
   b=int(stdin.readline())
   e1=0
   e1=bin(b).count("1")
   if(e1%2==0):
    print(e,end=" ")
    print(o)
   else:
    print(o,end=" ")
    print(e)
def __starting_point():
 main()
#a=5
#str1=""
#str1+=bin(a)
#print(str1[2:])

__starting_point()
