def clock_degree(stg):
    try:
        h, m = (int(n) for n in stg.split(":"))
        if not (0 <= h < 24 and 0 <= m < 60):
            raise ValueError
    except ValueError:
        return "Check your time !"
    return f"{((h % 12) or 12)* 30}:{(m or 60) * 6}"
