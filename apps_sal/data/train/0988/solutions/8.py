# # cook your dish here
# def more_frequent_item(lst):
#     new_lst = []
#     times = 0
#     for item in lst:
#         count_num = lst.count(item)
#         new_lst.append(count_num)
#         times = max(new_lst)
#     key = max(lst, key=lst.count)
#     return [key, times]
# try:
#     t = int(input())
#     for _ in range(t):
#         jk = int(input())
#         lst = list(map(int, input().split()))
#         Nlst = [0]*len(lst)
#         Nlst2 = [0]*len(lst)
#         z = more_frequent_item(lst)
#         if z[0] * z[1] > max(lst):
#             x = z[0]
#         else:
#             x = max(lst)
#         for i in range(len(lst)):
#             Nlst[i] = lst[i] ^ x
#         for j in range(len(lst)):
#             Nlst2[j] = lst[j] ^ z[0]
#         print(min(sum(Nlst), sum(Nlst2)))
# except:
#     pass4

from math import log2 
def findX(arr, n): 
 itr = arr[0] 
 for i in range(len(arr)): 
  if(arr[i] > itr): 
   itr = arr[i] 
 p = int(log2(itr)) + 1
 X = 0
 for i in range(p): 
  count = 0
  for j in range(n): 
   if (arr[j] & (1 << i)): 
    count += 1
  if (count > int(n / 2)): 
   X += 1 << i 
 sum = 0
 for i in range(n): 
  sum += (X ^ arr[i]) 
 print(sum)
def __starting_point(): 
 t = int(input())
 for _ in range(t):
  ss = int(input())
  arr = list(map(int, input().split()))
  n = len(arr) 
  findX(arr, n)
__starting_point()
