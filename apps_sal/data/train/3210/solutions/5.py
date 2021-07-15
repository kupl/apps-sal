def get_strings(s):
    return ','.join(f"{i}:{'*'*s.lower().count(i)}" for i in dict.fromkeys(s.replace(' ','').lower()))
