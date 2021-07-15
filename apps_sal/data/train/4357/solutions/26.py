def nth_smallest(arr, pos):
    arr=sorted(arr)
    for i,j in enumerate(arr):
       if i==pos-1:
          return j
