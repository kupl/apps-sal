def password(string):
    rules = [lambda s: any((x.isupper() for x in s)), lambda s: any((x.islower() for x in s)), lambda s: any((x.isdigit() for x in s)), lambda s: len(s) >= 8]
    if all((rule(string) for rule in rules)):
        return True
    else:
        return False
