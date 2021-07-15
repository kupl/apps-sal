def get_mean(arr,x,y):
  if x not in range(2,len(arr)+1) or y not in range(2, len(arr)+1): return -1
  return (sum(arr[:x])/x + sum(arr[-y:])/y) /2
