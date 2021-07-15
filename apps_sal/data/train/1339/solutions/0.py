# cook your dish here
def getAns(num):
    if num<10:return 2 
    last=int(str(num)[0]);rem=int(str(num)[1:]);steps=2;p=len(str(num))-1
    while True:
     steps+=rem//last+1;rem=rem%last 
     if last>0:rem=rem+10**p-last
     last=last-1
     if last==0:
      p=p-1;last=9
      if(len(str(rem))==1):rem=0
      else:rem=int(str(rem)[1:])
     if rem==0:            break
    return steps
for awa in range(int(input())):
    k=int(input())
    if(k==1):print(0)
    elif(k==2):print(9)
    elif(k==3):print(10)
    else:
     low,high,ans = 0,10**18,0
     while(low<=high):
      mid=(low+high)//2;temp=getAns(mid)
      if int(temp)==k:ans=max(ans,mid);low=mid+1 
      elif temp<k:low=mid+1 
      else:high=mid-1 
