def work_needed(projectMinutes, freeLancers):
    time = projectMinutes - sum(fl[0] * 60 + fl[1] for fl in freeLancers)
    if time <= 0:
        return "Easy Money!"
    else:
        return "I need to work {} hour(s) and {} minute(s)".format(time // 60, time % 60)
