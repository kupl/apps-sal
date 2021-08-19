def work_needed(projectMinutes, freeLancers):
    x = projectMinutes
    for flance in freeLancers:
        x -= flance[0] * 60 + flance[1]
    if x > 0:
        return 'I need to work ' + str(int(x / 60)) + ' hour(s) and ' + str(x % 60) + ' minute(s)'
    return 'Easy Money!'
