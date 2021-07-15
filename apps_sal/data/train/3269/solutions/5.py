def work_needed(projectMinutes, freeLancers):
    s = projectMinutes - sum(h * 60 + m for h, m in freeLancers)
    return 'Easy Money!' if s <= 0 else 'I need to work {} hour(s) and {} minute(s)'.format(*divmod(s, 60))
