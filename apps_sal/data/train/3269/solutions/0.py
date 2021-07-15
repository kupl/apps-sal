def work_needed(project_minutes, freelancers):
    available_minutes = sum(hours * 60 + minutes for hours, minutes in freelancers)
    workload_minutes = project_minutes - available_minutes
    if workload_minutes <= 0:
        return 'Easy Money!'
    else:
        hours, minutes = divmod(workload_minutes, 60)
        return 'I need to work {} hour(s) and {} minute(s)'.format(hours, minutes)
