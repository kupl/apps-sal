try:
 for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  x = int(input())

  left = 0
  right = n-1
  count1 = count2 = 0
  sum1=sum2=0
  
  while left<=right:
   if sum1<x*sum2:
    sum1 =sum1+arr[left]
    left +=1
    count1 +=1
    
   elif sum1>x*sum2:
    sum2 =sum2+ arr[right]
    right -=1
    count2 +=1
    
   else:
    if left!=right:
     sum1 =sum1+arr[left]
     left +=1
     count1 +=1
     
    elif count1<count2:
     sum2 =sum2+ arr[right]
     right -=1
     count2 =count2+1
     
    else:
     sum1 =sum1+arr[left]
     left +=1
     count1 +=1
     
  print(count1,count2)
except:
 pass
