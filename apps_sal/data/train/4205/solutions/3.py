def cannons_ready(gunners):
  return 'Fire!' if all(map(lambda x: x=='aye', gunners.values())) else 'Shiver me timbers!'
