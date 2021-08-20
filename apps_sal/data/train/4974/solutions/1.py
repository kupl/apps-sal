def user_contacts(data):
    return {u[0]: u[1] if len(u) > 1 else None for u in data}
