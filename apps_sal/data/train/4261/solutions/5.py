def robot_walk(a):
  aa=a[2::2]
  if aa!=sorted(aa,reverse=True):
      return True
  aa=a[1::2]
  if aa!=sorted(aa,reverse=True) or any(aa.count(i)>1 for i in aa):
      return True
  return False
