def braces_status(string):
    if "(]" in string or "(}" in string or "[)" in string or "[}" in string or "{)" in string or "{]" in string or string.count("(")!= string.count(")") or string.count("[")!= string.count("]") or string.count("{")!= string.count("}"):
        return False
    else:
        return True
