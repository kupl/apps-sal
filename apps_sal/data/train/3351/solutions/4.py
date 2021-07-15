def evil_code_medal(user_time, *medals):
    return next(
        (name for name, time in zip("Gold Silver Bronze".split(), medals) if user_time < time),
        "None")
