import re

pattern = re.compile(r"([A-Z]\d){5}\.-[A-Z]%\d\.\d\d\.")

def body_count(code):
    return bool(pattern.search(code))

