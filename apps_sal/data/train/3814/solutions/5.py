def get_military_time(stg):
    h, ms, ap = int(stg[:2]) % 12, stg[2:8], stg[8:]
    return f"{h + (12 if ap == 'PM' else 0):02d}{ms}"
