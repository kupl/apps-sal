def cannons_ready(gunners):
    # Fire! or Shiver me timbers!
    print(gunners)
    if 'nay' in gunners.values():
        return 'Shiver me timbers!'
    else:
        return 'Fire!'
