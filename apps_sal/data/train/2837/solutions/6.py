def what_is_the_time(time_in_mirror: str) -> str:
    h, m = list(map(int, time_in_mirror.split(":")))
    h, m = divmod(720 - m - (h % 12) * 60, 60)
    return f"{h or 12:02d}:{m:02d}"
