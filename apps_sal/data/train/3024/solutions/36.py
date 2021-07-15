def friend(x):
   friendly = lambda y: len(y)==4
   return list(filter(friendly,x))
