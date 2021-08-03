def work_needed(projectMinutes, freeLancers):
    diff = projectMinutes - sum(h * 60 + m for h, m in freeLancers)
    return "Easy Money!" if diff <= 0 else "I need to work {} hour(s) and {} minute(s)".format(diff // 60, diff % 60)
