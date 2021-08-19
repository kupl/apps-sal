def ant_bridge(w, s):
    return (lambda n: w[n:] + w[:n])(-len(''.join(__import__('re').findall('(?:-\\.+)+-', s))) % len(w))
