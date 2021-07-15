for t in range(eval(input())) :
 s, t = input(), input()
 s = s.lower()
 t = t.lower()
 if s < t :
  print('first')
 elif s > t :
  print('second')
 else :
  print('equal') 
