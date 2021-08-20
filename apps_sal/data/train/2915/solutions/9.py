def check_availability(sched, now):
    b = [t1 < now < t2 for (t1, t2) in sched]
    return sched[b.index(True)][1] if True in b else True
