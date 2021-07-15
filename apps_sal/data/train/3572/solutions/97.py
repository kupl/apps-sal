def invite_more_women(attendees):
    men = 0
    women = 0
    for sex in attendees:
        if sex == -1:
            women += 1
        else:
            men += 1
    if men > women:
        return True
    else:
        return False
