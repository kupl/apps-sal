def to12hourtime(hhmm):
    hh, mm = int(hhmm[:2]), int(hhmm[2:])
    return '{}:{:02} {}'.format(hh - 12 if hh > 12 else hh, mm, ['am','pm'][hh>=12]) if hh else '12:{:02} am'.format(mm)    
