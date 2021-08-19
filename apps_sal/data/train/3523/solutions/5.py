def password(s):
    return any((c.isupper() for c in s)) and any((c.islower() for c in s)) and any((c.isdigit() for c in s)) and (len(s) > 7)
