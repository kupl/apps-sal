def largest_arrangement(numbers):
  r=qsort(numbers)
  r=''.join([str(v) for v in r])
  return int(r)

def qsort(arr): 
  if len(arr) <= 1: return arr
  else:
    return qsort([x for x in arr[1:] if so(x,arr[0])==-1]) + [arr[0]] + qsort([x for x in arr[1:] if so(x,arr[0])!=-1])

def so(a,b):
  return -1 if str(b)+str(a) < str(a)+str(b) else 1
