def user_contacts(data):
    return {a : b[0] if b else None for a, *b in data}
