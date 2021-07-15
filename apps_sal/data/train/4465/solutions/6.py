def super_size(n):
  arr = list(map(int,str(n)))
  arr.sort(reverse=True)
  strings = [str(integer) for integer in arr]
  a_string = "".join(strings)
  an_integer = int(a_string)
  return an_integer
