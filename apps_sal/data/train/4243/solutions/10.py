def find_average(array):
  mean=0
  if len(array)== 0:
    return mean
  sum=0
  for i in array:
    sum= sum+i
  mean= sum/(len(array))
  return mean

