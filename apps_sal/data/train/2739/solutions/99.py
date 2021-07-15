def cube_odd(arr):
  s=0
  arr1=[]
  for i in arr:
    if (type(i)==str or type(i)==bool):
      return None
      break
    else:
      arr1.append(i)
  for i in range(len(arr1)):
    if (arr1[i]%2==1):
      s+=arr1[i]**3
  return s
