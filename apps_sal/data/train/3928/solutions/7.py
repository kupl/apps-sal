def billboard(name, price=30):
  
  # fine, dammit! I won't use that confounded * operator,
  # but you're paying the inefficiency costs...
  return sum(price for _ in name)
