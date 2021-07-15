def cannons_ready(gunners): 
  return 'Shiver me timbers!' if [value for value in gunners.values()].count('nay') >= 1 else 'Fire!'
