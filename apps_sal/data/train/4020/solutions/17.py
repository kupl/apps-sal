def validate_hello(greetings):
    import re
    return True if re.findall("h[oae]l{1,2}[oa]|ciao|salut|ahoj|czesc", greetings, re.IGNORECASE) else False
