def band_name_generator(s):
    return (('The ' if s[0] != s[-1] else s[:-1]) + s).title()
