def greet(name, owner):
    f_name = name.lower()
    f_owner = owner.lower()
    if f_name == f_owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
