for i in range(int(input())):
 s = input()
 l = list(input())
 l = list([x for x in l if x != '.'])
 if 'T' in l[::2] or 'H' in l[1::2] or len(l)%2 != 0:
  print('Invalid')
 else:
  print('Valid')

