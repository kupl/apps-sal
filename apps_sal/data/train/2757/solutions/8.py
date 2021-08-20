from string import digits as D, ascii_lowercase as L, ascii_uppercase as U
S = '!@#$%^&*?'


def check_password(s):
    return 'valid' if 8 <= len(s) <= 20 and all((c in D + L + U + S for c in s)) and any((c in D for c in s)) and any((c in L for c in s)) and any((c in U for c in s)) and any((c in S for c in s)) else 'not valid'
