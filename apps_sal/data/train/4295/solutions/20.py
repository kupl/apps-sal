def balanced_num(number):
  n = list(map(int,str(number)))
  l = (len(n)-1,len(n)-2)[len(n) % 2 == 0]//2
  return "Balanced" if number <=99 else ("Not Balanced","Balanced")[sum(n[:l]) == sum(n[-l:])]

