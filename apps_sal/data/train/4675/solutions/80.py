def set_alarm(employed: bool, vacation: bool) -> bool:
    return employed and (not vacation)
