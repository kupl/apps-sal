def nickname_generator(name):
    return (name[:4] if name[2] in "aeiou" else name[:3]) if len(name) > 3 else "Error: Name too short"
