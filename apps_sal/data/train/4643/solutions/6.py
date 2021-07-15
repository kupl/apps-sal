REGEX = __import__("re").compile(r"[1-46]\d{5}").fullmatch

def zipvalidate(postcode):
    return bool(REGEX(postcode))
