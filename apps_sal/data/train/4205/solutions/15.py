def cannons_ready(gunners):
  return next(('Shiver me timbers!' for x in gunners.values() if x == 'nay'), 'Fire!')
