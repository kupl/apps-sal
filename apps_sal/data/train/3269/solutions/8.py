def work_needed(projectMinutes, freeLancers):
    req = projectMinutes - sum(60 * f[0] + f[1] for f in freeLancers)
    if req <= 0:
        return 'Easy Money!'
    return f"I need to work {req//60} hour(s) and {req%60} minute(s)"
