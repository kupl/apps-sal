def cannons_ready(gunners):
    return 'Fire!' if all(map(lambda x: x[1]=='aye', gunners.items())) else 'Shiver me timbers!'
