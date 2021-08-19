def highlight(s):
    return __import__('re').sub('([FLR])\\1*|\\d+', lambda m: '<span style="color: %s">%s</span>' % ({'F': 'pink', 'L': 'red', 'R': 'green'}.get(m.group()[0], 'orange'), m.group()), s)
