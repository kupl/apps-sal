def first_non_repeating_letter(s):
    return ([c for c in s if s.lower().find(c.lower()) == s.lower().rfind(c.lower())] or [""])[0]
