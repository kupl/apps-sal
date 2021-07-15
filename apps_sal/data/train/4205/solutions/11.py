def cannons_ready(gunners):
  return all(x == 'aye' for x in gunners.values()) and 'Fire!' or 'Shiver me timbers!'
