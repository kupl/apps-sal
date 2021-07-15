def nickname_generator(name):
    if len(name) < 4:
        return 'Error: Name too short'
    return name[: 4 if name[2] in 'aeiou' else 3]
