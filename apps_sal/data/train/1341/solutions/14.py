def bin_search1(arr, x):
 s = 0
 e = len(arr)-1
 while s <= e:
  m = (s+e)//2
  if arr[m] > x:
   e = m-1
  else:
   s = m+1
  # print(s, e)
 # print(s)
 return s


def bin_search2(arr, x):
 s = 0
 e = len(arr)-1
 while s <= e:
  m = (s+e)//2
  if arr[m] >= x:
   e = m-1
  else:
   s = m+1
  # print(s, e)
 # print(s)
 return s





t = int(input())
for i in range(t):
 n = int(input())
 arr = [int(j) for j in input().split()]
 var = 0
 flag = 0
 for i in range(n-1):
  if arr[i+1] <= arr[i]:
   var = 1
   ind1 = i
   break

 if var == 0:
  print((n*(n+1))//2 -1)
  continue


 for i in range(n-1, 0, -1):
  if arr[i-1] >= arr[i]:
   ind2 = i
   break

 # print(ind1, ind2)
 arr1 = arr[:ind1+1]
 arr2 = arr[ind2:]

 # print(arr1, arr2)

 count = len(arr1) + len(arr2)
 for i in range(len(arr1)):
  x = bin_search1(arr2, arr1[i])
  # print(x)
  count += len(arr2)+1-x

 # print(count)
 for i in range(len(arr2)):
  x = bin_search1(arr1, arr2[i])
  # print(x)
  count += x+1

 print(count//2)





