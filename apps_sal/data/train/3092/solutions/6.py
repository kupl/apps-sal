def denumerate(enum_list):
    try:
        return bool(enum_list) and ''.join(c for cnt, (idx, c) in enumerate(sorted(enum_list)) if cnt == idx and len(c) == 1 and c.isalnum() or 1 / 0)
    except:
        return False
