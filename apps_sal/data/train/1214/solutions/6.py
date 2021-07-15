T=int(input())
i=1
while T:
 T-=1;
 M,N=map(int,input().split())
 cur_x,cur_y=0,0
 dest_x,dest_y=map(int,input().split())
 L=int(input())
 direction_seqn=input()
 for direction in direction_seqn:
  if direction=='U':
   cur_y+=1
  elif direction=='D':
   cur_y-=1
  elif direction=='R':
   cur_x+=1
  elif direction=='L':
   cur_x-=1
 print("Case "+str(i)+": ",end="");i+=1
 if (cur_x,cur_y)==(dest_x, dest_y):
   print("REACHED")
 elif cur_x<0 or cur_x>M or cur_y<0 or cur_y>N:
   print("DANGER")
 else:
   print("SOMEWHERE")

  
 
