def cannons_ready(gunners):
  # Fire! or Shiver me timbers!
    if list(gunners.values()).count('nay') == 0:
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
