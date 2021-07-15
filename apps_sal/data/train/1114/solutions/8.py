# def main():
#     t=int(input())
#     while(t!=0):
#         n = int(input())
#         arr = list(map(int, input().split()))
#         maxVal=-1
#         for i in range(0,n):
#             for j in range(i+1,n):
#                 temp =arr[i]+arr[j]
#                 if(maxVal<temp):
#                     maxVal=temp
#
#         count=0
#         for i in range(0,n):
#             for j in range(i+1,n):
#                 temp =arr[i]+arr[j]
#                 if(maxVal==temp):
#                     count+=1
#         val = (n*(n-1))/2
#         print(count/val)
#         t=t-1
#
# def __starting_point():
#     main()


def main():
 t=int(input())
 while(t!=0):
  n = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  maxEle = arr[n-1]
  num = (n*(n-1))/2
  count1= arr.count(maxEle)

  if(count1==1):
   count2=arr.count(arr[n-2])
   print(count2/num)
  else:
   val = (count1*(count1-1))/2
   print(val/num)
  t=t-1

def __starting_point():
 main()
__starting_point()
