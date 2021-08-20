def user_contacts(data):
    return {name: code[0] if code else None for (name, *code) in data}
