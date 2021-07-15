def nickname_generator(name):
        if len(name) > 3:
            return name[:4] if name[2] in 'aeiou' else name[:3]
        else:
            return 'Error: Name too short'
