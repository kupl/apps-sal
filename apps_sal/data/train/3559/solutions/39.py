def chromosome_check(sperm):
    count = 0
    for i in sperm:
        if i == 'Y':
            count += 1
    if count == 1:
        return "Congratulations! You're going to have a son."
    else:
        return "Congratulations! You're going to have a daughter."
