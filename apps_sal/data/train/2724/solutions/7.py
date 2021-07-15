def kebabize(string):
  return ''.join(c if c.islower() else f'-{c.lower()}' for c in [c for c in string if c.isalpha()]).strip('-')
