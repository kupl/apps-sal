def reverse_list(l):
  return [int(i) for i in ''.join(str(n) for n in l[::-1])]
