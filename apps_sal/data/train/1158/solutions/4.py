

def check(s):
 d3=d5=d8=0
 for c in s:
  if not c.isdigit():
   continue
  if c=="3":d3+=1
  elif c=="5":d5+=1
  elif c=="8":d8+=1
  else:return False
 #print d3,d5,d8
 return d3<=d5<=d8

def main():
 cnt=0
 for i in range(int(input())):
  s=input().split(" ")[-1]
  #print s
  if check(s):
   #print s
   cnt+=1
 print(cnt)

main()
