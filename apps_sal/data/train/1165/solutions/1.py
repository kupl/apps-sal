from collections import defaultdict
def solve(date,m):

 arr = [31,29,31,30,31,30,31,31,30,31,30,31]
 copied = arr.copy()
 
 d = {
 "january": 0,
 "february": 1,
 "march": 2,
 "april": 3,
 "may": 4,
 "june": 5,
 "july": 6,
 "august":7,
 "september": 8,
 "october": 9,
 "november":10,
 "december": 11
 }

 month = d[m]

 total = 366//2
 i = month
 total += date

 while(total > 0):
  
  while(arr[i]>0 ):
   if(total<= arr[i]):
    return give(total, i,d)
   else:
    total = total - arr[i]
    i = (i+1) %12
    break


def give(day, month, d):
 temp = None 

 for x in d:
  if(d[x] == month):
   temp = x

 print("{} {}".format(day,temp))

t = int(input())
for _ in range(t):
 d,m = map(str, input().split())

 solve(int(d), m)
