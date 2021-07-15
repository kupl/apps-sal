def check_exam(arr1,arr2):
    return max(0, sum(4 if a1 == a2 else -1 for a1, a2 in zip(arr1, arr2) if a2))
  

