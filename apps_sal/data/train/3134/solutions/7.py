def is_valid(idn):
    return len(idn) > 0 and idn[0].lower() in '$_abcdefghijklmnopqrstuvwxyz' and all([l.lower() in '$_abcdefghijklmnopqrstuvwxyz0123456789' for l in idn[1:]])
