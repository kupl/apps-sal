def find_longest(arr):
    number = 0
    length = 0
    for x in arr:
      if len(str(x)) > length:
        length = len(str(x))
        number = x
    return number
