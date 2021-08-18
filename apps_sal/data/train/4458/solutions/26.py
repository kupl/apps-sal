def time_correct(t):
    if not t:
        return t
    for i in t:
        if i not in "1234567890:":
            return None
    slot = t.split(":")
    for k, i in enumerate(slot):
        try:
            if len(slot[k]) > 2:
                return None
            slot[k] = int(slot[k])
        except ValueError:
            return None
    if len(slot) != 3:
        return None
    slot[1] += slot[2] // 60
    slot[0] += slot[1] // 60
    slot[2] = slot[2] % 60
    slot[1] = slot[1] % 60
    slot[0] = slot[0] % 24
    return ":".join([str(x).zfill(2) for x in slot])
