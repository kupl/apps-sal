def bus_timer(time):
    hh, mm = time.split(':')
    hh, mm = int(hh), int(mm)
    
    if hh == 23:
        if mm <= 55: return 10 - mm % 15 if mm % 15 <= 10 else 15 - (mm % 15 - 10)
        else: return 5 * 60 + 55 + (60 - mm)
    elif 6 <= hh:
        return 10 - mm % 15 if mm % 15 <= 10 else 15 - (mm % 15 - 10)
    
    return ((5 - hh) * 60) + (55 - mm) if hh < 5 or (hh == 5 and mm <= 55) else 15 - (mm % 15 - 10)

