def reverse_letter(string):
  iaprw = []
  for i in string:
    if i.isalpha() == True:
      iaprw.append(i)
  iaprw.reverse()
  return ''.join(iaprw)
