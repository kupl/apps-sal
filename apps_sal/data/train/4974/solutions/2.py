def user_contacts(data):
    a = {}
    for i in data:
        a[i[0]] = i[1] if len(i) == 2 else None
    return a
