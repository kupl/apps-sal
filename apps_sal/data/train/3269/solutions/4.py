def work_needed(project, freelancers):
    to_work = project - sum((h * 60 + m for (h, m) in freelancers))
    return 'I need to work {} hour(s) and {} minute(s)'.format(*divmod(to_work, 60)) if to_work > 0 else 'Easy Money!'
