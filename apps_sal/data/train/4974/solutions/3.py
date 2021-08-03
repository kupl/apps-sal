def user_contacts(data):
    return {p[0]: p[1] if len(p) > 1 else None for p in data}
