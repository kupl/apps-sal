def cannons_ready(reply):
    xx = [x for x in reply.values()].count('aye')
    if xx == len(reply):
        return 'Fire!'
    else:
        return 'Shiver me timbers!'
