def next_letter(s):
    return s.translate(str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                     'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA'))
