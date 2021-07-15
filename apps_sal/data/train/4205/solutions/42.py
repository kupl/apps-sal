def cannons_ready(gunners):
    for d in list(gunners.values()):
        if d !='aye':
            return 'Shiver me timbers!'
    return 'Fire!'
  # Fire! or Shiver me timbers!

