def user_contacts(data):
    return {l[0]: l[1] if len(l) > 1 else None for l in data}
