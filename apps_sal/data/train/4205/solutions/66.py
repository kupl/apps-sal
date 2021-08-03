def cannons_ready(gunners):
    return ['Shiver me timbers!', 'Fire!'][all(ans == 'aye' for ans in list(gunners.values()))]
