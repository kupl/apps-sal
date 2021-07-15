# cook your dish here
# T = int(input())
# while T>0:
#     s = list(input())
#     l = len(s)
#     for i in range(l):
#       if s[i]=='m' and i>0 and s[i-1]=='s':
#           s[i-1]='*'
#       elif s[i]=='m' and i<l-1 and s[i+1]=='s':
#           s[i+1]='*'
#     a=s.count('s')
#     b=s.count('m')
#     if a>b:
#         print("snakes")
#     elif b>a:
#         print("mangooses")
#     else:
#         print("tie")
#     T-=1

for h in range(int(input())):
 s=input()
 mc=s.count('m')
 l=list(s)
 k=0
 for i in range(len(l)):
  if(l[i]=='m'):
   if l[i-1]=='s' and i>0:
     l[i-1]='0'
     
   elif(i<(len(s)-1))and l[i+1]=='s': 
    l[i+1]='0'
  
 sc=l.count('s')

 if mc>sc:
  print('mongooses')
 elif sc>mc:
  print('snakes')
 else:
  print('tie')
