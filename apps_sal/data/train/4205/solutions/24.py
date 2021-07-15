def cannons_ready(gunners):
    all = []
    yes = []
    no = []
    for key in gunners:
        all.append(gunners[key])
    for i in all:
        if i == 'aye':
            yes.append(i)
        if i == 'nay':
            no.append(i)
    if len(no) == 0: return 'Fire!'
    else: return 'Shiver me timbers!'
    
    
'''If all answers are 'aye' then Fire! if one or more are 'nay' then Shiver me timbers!'''
