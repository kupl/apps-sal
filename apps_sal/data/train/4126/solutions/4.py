def what_time_is_it(angle):
    q, r = divmod(angle, 30)
    return f"{int(q) or 12:02d}:{int(2*r):02d}"
