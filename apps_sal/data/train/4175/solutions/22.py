def repeater(string, n):
    # Your code goes here.
  collection = []
  while n > 0:
    collection.append(string)
    n -= 1
  return(''.join(collection))

