year_days = lambda y: "%s has %s days" % (y, __import__("calendar").isleap(y) + 365)

