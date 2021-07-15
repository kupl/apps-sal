def check_exam(arr1,arr2):
    total = 0
    for x, y in zip(arr1, arr2):
        if x == y: total += 4
        elif y:    total -= 1
    return total if total > 0 else 0
  

