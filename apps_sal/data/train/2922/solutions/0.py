def crap(garden, bags, cap):
    cap *= bags
    for turf in garden:
        if 'D' in turf: return 'Dog!!'
        cap -= turf.count('@')
    return 'Cr@p' if cap < 0 else 'Clean'
