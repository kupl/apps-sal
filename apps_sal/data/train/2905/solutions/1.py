def nickname_generator(name):
    return name[:3 + (name[2] in 'aeiou')] if len(name) > 3 else 'Error: Name too short'
