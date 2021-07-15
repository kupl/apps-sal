def spread(func, args):
  return eval('func'+ '('+','.join(str(a) for a in args)+')')
