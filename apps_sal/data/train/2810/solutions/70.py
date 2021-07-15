def solve(arr):
    return [ sum( i == ord(l)-97  for i,l in enumerate(word.lower())) for word in arr]
