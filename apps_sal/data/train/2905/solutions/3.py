def nickname_generator(name):
    if len(name) < 4:
        return 'Error: Name too short'
    elif name[2] not in 'aeiou':
        return name[:3]
    elif name[2] in 'aeiou':
        return name[:4]
