def make_readable(seconds):
    h= seconds/60**2
    m= (seconds%60**2)/60
    s= (seconds%60**2%60)
    return "%02d:%02d:%02d" % (h, m, s)
    # Do something

