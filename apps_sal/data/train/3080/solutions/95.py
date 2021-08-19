def who_is_paying(name):
    s = []
    if len(name) > 2:
        s.append(name)
        izi = name[:2]
        s.append(izi)
        return s
    if len(name) <= 2:
        s.append(name)
        return s


who_is_paying('')
