def what_time_is_it(angle: float) -> str:
    h, m = list(map(int, divmod(2 * angle, 60)))
    return f"{h or 12:02d}:{m:02d}"
