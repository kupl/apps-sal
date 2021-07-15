def sequence_classifier(arr):
  f,l=0,len(arr)-1
  for i in range(0,l): f|= 1 if arr[i]<arr[i+1] else 2 if arr[i]==arr[i+1] else 4
  return [0,1,5,2,3,0,4,0][f]
