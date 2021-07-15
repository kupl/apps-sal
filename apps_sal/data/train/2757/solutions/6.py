import re
def check_password(s):
    if len(s) > 20 or len(s) < 8: return "not valid"
    a1 = bool(re.search(r'[A-Z]', s))
    a2 = bool(re.search(r'[a-z]', s))
    a3 = bool(re.search(r'\d', s))
    a4 = bool(re.search(r'[!@#$%^&*?]', s))
    a5 = bool(re.search(r'^[A-Za-z!@#$%^&*?\d]*$', s))
    return "valid" if a1*a2*a3*a4*a5 else "not valid"
