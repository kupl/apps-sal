import re
def zipvalidate(postcode):
    return bool(re.fullmatch(r"[1-46]\d{5}", postcode))
