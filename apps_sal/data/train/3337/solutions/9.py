def bracket_buster(string):
    # Get after it!
    if string == None or not isinstance(string, str):
        return "Take a seat on the bench."
    import re
    pattern = re.compile(r'\[([\w\s\'?!\d\-]+|\[{1,}|'')\]', re.I)
    mo = pattern.findall(string)
    return mo
