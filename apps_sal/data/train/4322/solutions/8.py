from re import search
def body_count(code):
    return bool(search("([A-Z]\d){5}\.\-[A-Z]%\d\.\d\d\.",code))
