def cannons_ready(gunners):
    # Fire! or Shiver me timbers!
    if 'nay' in gunners.values():
        return 'Shiver me timbers!'
    else:
        return 'Fire!'


cannons_ready({'m': 'a'})
