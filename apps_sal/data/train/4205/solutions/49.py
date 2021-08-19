def cannons_ready(gunners):
    return ['Fire!', 'Shiver me timbers!']['nay' in list(gunners.values())]
#     return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'
