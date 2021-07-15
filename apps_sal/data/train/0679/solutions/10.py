# bit_cracker007 #
test=eval(input())
exer_book=[]
min_stack=[]
top=-1
for i in range(test):
 s=input().split() 
 if(s[0]!="-1" and s[0]!="0"):
  n=int(s[0])
  if top >=0 and n > exer_book[top][0] :            
   min_stack[top]+=1 # if current > last then no insertion              ,number of min book removes incr. by 1
  else:
   exer_book.append((n,s[1])) 
   min_stack.append(0) # if current < last min no of current               min book to remove = 0
   top+=1 
 elif(s[0]=="-1"):      
  print("%s %s" %(min_stack[top],exer_book[top][1]))
  exer_book.pop()
  min_stack.pop()
  top-=1 
