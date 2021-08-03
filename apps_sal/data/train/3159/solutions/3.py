def is_odd_heavy(xs):
    return bool(xs) and (
        min((x for x in xs if x % 2 == 1), default=min(xs) - 1) >
        max((x for x in xs if x % 2 == 0), default=min(xs) - 1)
    )
