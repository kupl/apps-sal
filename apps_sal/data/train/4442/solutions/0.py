def case_sensitive(s):
    return [s.islower() or not s, [c for c in s if c.isupper()]]
