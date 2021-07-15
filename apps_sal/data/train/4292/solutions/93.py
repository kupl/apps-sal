def string_clean(s):
    import re
    matches = re.finditer("[a-zA-Z~#\$%^&!@*():;\"'\.,?\s]",s)
    return "".join([match.group() for match in matches])
