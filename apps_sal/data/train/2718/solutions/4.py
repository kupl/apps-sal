def timed_reading(m, t):
    return len([e for e in __import__('re').findall('\\w+', t) if len(e) <= m])
