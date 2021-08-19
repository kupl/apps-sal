def cannons_ready(gunners):
  # Fire! or Shiver me timbers!
    if len(set(gunners.values())) >= 2:
        return 'Shiver me timbers!'
    return 'Fire!'
